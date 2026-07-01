from datetime import datetime
from pathlib import Path


def log_access(name: str, status: str, file_path: str = "data/attendance.csv") -> None:
    """
    Enregistre un événement d'accès dans un fichier CSV.

    name : nom de l'utilisateur reconnu ou UNKNOWN
    status : AUTHORIZED ou REFUSED
    file_path : chemin du fichier CSV
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text("name,status,time\n", encoding="utf-8")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{name},{status},{now}\n")