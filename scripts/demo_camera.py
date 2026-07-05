"""
Démonstration caméra OpenCV.

Objectif :
- ouvrir la caméra ;
- afficher le flux vidéo ;
- quitter avec la touche q.

Commande :
python scripts/demo_camera.py
"""

from smart_door_lock.camera import CameraReadError, CameraService
from smart_door_lock.opencv_camera import create_opencv_camera_capture


def main() -> None:
    try:
        import cv2
    except ImportError as error:
        raise SystemExit(
            "OpenCV n'est pas installé. Installe-le avec : "
            "python -m pip install opencv-python"
        ) from error

    camera_capture = create_opencv_camera_capture(camera_index=0)
    camera_service = CameraService(camera_capture)

    print("Caméra démarrée.")
    print("Appuie sur q pour quitter.")

    try:
        while True:
            try:
                frame = camera_service.read_frame()
            except CameraReadError as error:
                print(f"Erreur caméra : {error}")
                break

            cv2.imshow("Demo camera - Smart Door Lock", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera_service.release()
        cv2.destroyAllWindows()
        print("Caméra arrêtée proprement.")


if __name__ == "__main__":
    main()