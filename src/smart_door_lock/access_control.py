def is_access_authorized(distance: float, threshold: float = 0.55) -> bool:
    """
    Retourne True si la distance faciale est inférieure au seuil.

    Plus la distance est faible, plus le visage détecté correspond
    à une personne enregistrée.
    """
    return distance < threshold