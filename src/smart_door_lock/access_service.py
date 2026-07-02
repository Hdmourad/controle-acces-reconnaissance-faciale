from smart_door_lock.access_control import is_access_authorized


def handle_access_request(
    name: str | None,
    distance: float | None,
    lock_controller,
    logger,
    threshold: float = 0.55,
) -> dict:
    """
    Traite une demande d'accès à partir du résultat de reconnaissance faciale.

    Si l'utilisateur est reconnu et que la distance est inférieure au seuil :
    - accès autorisé
    - ouverture de la serrure
    - journalisation AUTHORIZED

    Sinon :
    - accès refusé
    - serrure fermée
    - journalisation REFUSED
    """
    if name is not None and distance is not None and is_access_authorized(distance, threshold):
        normalized_name = name.upper()
        lock_controller.open_lock()
        logger(normalized_name, "AUTHORIZED")

        return {
            "name": normalized_name,
            "status": "AUTHORIZED",
            "opened": True,
        }

    logger("UNKNOWN", "REFUSED")

    return {
        "name": "UNKNOWN",
        "status": "REFUSED",
        "opened": False,
    }