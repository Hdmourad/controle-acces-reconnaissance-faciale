from pathlib import Path

from smart_door_lock.config import ALLOWED_IMAGE_EXTENSIONS


def is_supported_image_file(file_path: str | Path) -> bool:
    """
    Vérifie si un fichier est une image supportée.
    """
    return Path(file_path).suffix.lower() in ALLOWED_IMAGE_EXTENSIONS


def extract_person_name_from_file(file_path: str | Path) -> str:
    """
    Extrait le nom de la personne à partir du nom du fichier.

    Exemple :
    data/known_faces/Mourad_Hadji.jpg -> Mourad Hadji
    """
    file_name = Path(file_path).stem
    return file_name.replace("_", " ").replace("-", " ").strip()


def list_known_face_files(directory: str | Path) -> list[Path]:
    """
    Retourne la liste des images valides dans le dossier des visages connus.
    """
    directory_path = Path(directory)

    if not directory_path.exists():
        return []

    return sorted(
        file_path
        for file_path in directory_path.iterdir()
        if file_path.is_file() and is_supported_image_file(file_path)
    )


def load_known_face_names(directory: str | Path) -> list[str]:
    """
    Retourne les noms des personnes enregistrées dans le dossier.
    """
    face_files = list_known_face_files(directory)
    return [extract_person_name_from_file(file_path) for file_path in face_files]