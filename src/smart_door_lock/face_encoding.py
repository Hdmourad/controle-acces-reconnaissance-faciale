from pathlib import Path
from typing import Any


def load_image_with_backend(image_path: str | Path, image_loader) -> Any:
    """
    Charge une image avec un backend externe.

    Exemple de backend réel :
    face_recognition.load_image_file

    Cette fonction est testable car le backend est injecté.
    """
    return image_loader(str(image_path))


def encode_face_with_backend(image, face_encoder) -> Any | None:
    """
    Génère l'encodage facial d'une image.

    Retourne None si aucun visage n'est détecté.
    """
    encodings = face_encoder(image)

    if len(encodings) == 0:
        return None

    return encodings[0]


def build_known_face_encoding(image_path: str | Path, image_loader, face_encoder):
    """
    Charge une image puis retourne son encodage facial.
    """
    image = load_image_with_backend(image_path, image_loader)
    return encode_face_with_backend(image, face_encoder)