from smart_door_lock.config import FACE_DISTANCE_THRESHOLD
from smart_door_lock.workflow import process_face_access


class DemoLockController:
    """
    Contrôleur de serrure simulé pour tester le workflow sans Raspberry Pi.
    """

    def __init__(self):
        self.opened = False

    def open_lock(self):
        self.opened = True
        print("Serrure simulée : ouverture autorisée")


def demo_logger(name: str, status: str) -> None:
    """
    Journalisation simulée pour afficher le résultat dans le terminal.
    """
    print(f"Journal d'accès : {name} - {status}")


def run_demo_access():
    """
    Lance une démonstration simple du système.
    """
    known_names = ["Bill Gates", "Mourad Hadji", "Jack Ma"]
    face_distances = [0.80, 0.42, 0.67]

    lock_controller = DemoLockController()

    result = process_face_access(
        known_names=known_names,
        face_distances=face_distances,
        lock_controller=lock_controller,
        logger=demo_logger,
        threshold=FACE_DISTANCE_THRESHOLD,
    )

    return result


def main():
    print("Démarrage du système Smart Door Lock")
    result = run_demo_access()
    print(f"Résultat final : {result}")


if __name__ == "__main__":
    main()