"""
Démonstration complète du contrôle d'accès.

Objectif :
- charger les visages connus depuis data/known_faces ;
- ouvrir la caméra ;
- détecter un visage ;
- comparer avec les utilisateurs autorisés ;
- autoriser ou refuser l'accès ;
- enregistrer l'événement dans data/attendance.csv.

Commande avec serrure simulée :
python scripts/demo_access_control.py

Commande avec GPIO réel Raspberry Pi :
python scripts/demo_access_control.py --real-gpio
"""

import argparse
import time
from pathlib import Path

from smart_door_lock.access_service import handle_access_request
from smart_door_lock.camera import CameraReadError, CameraService
from smart_door_lock.config import (
    ATTENDANCE_FILE_PATH,
    FACE_DISTANCE_THRESHOLD,
    KNOWN_FACES_DIR,
)
from smart_door_lock.database import log_access
from smart_door_lock.face_recognition_adapter import (
    compute_face_distances,
    extract_face_encodings,
    load_image,
)
from smart_door_lock.face_repository import (
    extract_person_name_from_file,
    list_known_face_files,
)
from smart_door_lock.opencv_camera import create_opencv_camera_capture
from smart_door_lock.raspberry_gpio_lock import create_raspberry_pi_lock_controller
from smart_door_lock.recognition import identify_face


class SimulatedLockController:
    """
    Contrôleur de serrure simulé.

    Il permet de faire une démonstration sur PC sans Raspberry Pi
    et sans serrure réelle.
    """

    def open_lock(self) -> None:
        print("Serrure simulée : ouverture pendant quelques secondes.")


def load_known_faces(known_faces_dir: str):
    """
    Charge les images des utilisateurs autorisés et extrait leurs encodages faciaux.
    """
    face_files = list_known_face_files(known_faces_dir)

    known_names = []
    known_encodings = []

    for face_file in face_files:
        person_name = extract_person_name_from_file(face_file)

        try:
            image = load_image(str(face_file))
            image_encodings = extract_face_encodings(image)
        except ModuleNotFoundError as error:
            raise SystemExit(
                "La bibliothèque face_recognition n'est pas installée. "
                "Installe-la avec : python -m pip install face-recognition"
            ) from error

        if len(image_encodings) == 0:
            print(f"Aucun visage détecté dans : {face_file}")
            continue

        known_names.append(person_name)
        known_encodings.append(image_encodings[0])

        print(f"Utilisateur chargé : {person_name}")

    return known_names, known_encodings


def create_lock_controller(use_real_gpio: bool):
    """
    Crée le contrôleur de serrure.

    Par défaut, la serrure est simulée.
    Avec --real-gpio, le GPIO Raspberry Pi est utilisé.
    """
    if use_real_gpio:
        return create_raspberry_pi_lock_controller()

    return SimulatedLockController()


def run_demo(
    known_faces_dir: str,
    threshold: float,
    use_real_gpio: bool,
    camera_index: int,
) -> None:
    try:
        import cv2
    except ImportError as error:
        raise SystemExit(
            "OpenCV n'est pas installé. Installe-le avec : "
            "python -m pip install opencv-python"
        ) from error

    known_names, known_encodings = load_known_faces(known_faces_dir)

    if len(known_names) == 0:
        raise SystemExit(
            "Aucun utilisateur autorisé chargé. "
            "Ajoute au moins une image dans data/known_faces, par exemple : "
            "Mourad_Hadji.jpg"
        )

    lock_controller = create_lock_controller(use_real_gpio)

    camera_capture = create_opencv_camera_capture(camera_index=camera_index)
    camera_service = CameraService(camera_capture)

    print("Démonstration contrôle d'accès démarrée.")
    print("Appuie sur q pour quitter.")
    print("Présente un visage devant la caméra.")

    try:
        while True:
            try:
                frame = camera_service.read_frame()
            except CameraReadError as error:
                print(f"Erreur caméra : {error}")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            detected_encodings = extract_face_encodings(rgb_frame)

            display_text = "Aucun visage détecté"

            if len(detected_encodings) > 0:
                detected_encoding = detected_encodings[0]

                distances = compute_face_distances(
                    known_encodings,
                    detected_encoding,
                )

                recognition_result = identify_face(
                    known_names=known_names,
                    face_distances=distances,
                    threshold=threshold,
                )

                access_result = handle_access_request(
                    name=recognition_result["name"],
                    distance=recognition_result["distance"],
                    lock_controller=lock_controller,
                    logger=lambda name, status: log_access(
                        name,
                        status,
                        ATTENDANCE_FILE_PATH,
                    ),
                    threshold=threshold,
                )

                display_text = (
                    f"{access_result['name']} - "
                    f"{access_result['status']}"
                )

                print(f"Résultat : {access_result}")

                cv2.putText(
                    frame,
                    display_text,
                    (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0) if access_result["opened"] else (0, 0, 255),
                    2,
                )

                cv2.imshow("Demo access control - Smart Door Lock", frame)
                cv2.waitKey(2000)
                break

            cv2.putText(
                frame,
                display_text,
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            cv2.imshow("Demo access control - Smart Door Lock", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            time.sleep(0.05)

    finally:
        camera_service.release()
        cv2.destroyAllWindows()
        print("Démonstration terminée proprement.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Démonstration du système de contrôle d'accès facial."
    )

    parser.add_argument(
        "--known-faces-dir",
        default=KNOWN_FACES_DIR,
        help="Dossier contenant les images des utilisateurs autorisés.",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=FACE_DISTANCE_THRESHOLD,
        help="Seuil de reconnaissance faciale.",
    )

    parser.add_argument(
        "--camera-index",
        type=int,
        default=0,
        help="Index de la caméra OpenCV.",
    )

    parser.add_argument(
        "--real-gpio",
        action="store_true",
        help="Utiliser le vrai GPIO Raspberry Pi au lieu de la serrure simulée.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    run_demo(
        known_faces_dir=args.known_faces_dir,
        threshold=args.threshold,
        use_real_gpio=args.real_gpio,
        camera_index=args.camera_index,
    )


if __name__ == "__main__":
    main()