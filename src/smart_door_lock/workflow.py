from smart_door_lock.access_service import handle_access_request
from smart_door_lock.recognition import identify_face


def process_face_access(
    known_names,
    face_distances,
    lock_controller,
    logger,
    threshold: float = 0.55,
):
    """
    Traite un accès complet à partir des distances faciales.

    Étapes :
    1. Identifier la meilleure correspondance faciale.
    2. Vérifier si la distance est acceptable.
    3. Autoriser ou refuser l'accès.
    4. Ouvrir la serrure si l'accès est autorisé.
    5. Journaliser l'événement.
    """
    recognition_result = identify_face(
        known_names=known_names,
        face_distances=face_distances,
        threshold=threshold,
    )

    return handle_access_request(
        name=recognition_result["name"],
        distance=recognition_result["distance"],
        lock_controller=lock_controller,
        logger=logger,
        threshold=threshold,
    )