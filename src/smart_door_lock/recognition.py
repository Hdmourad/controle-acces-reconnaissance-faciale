import numpy as np


def get_best_match_index(face_distances):
    """
    Retourne l'index de la distance faciale la plus faible.

    Plus la distance est faible, plus le visage détecté est proche
    d'un visage connu.
    """
    if len(face_distances) == 0:
        return None

    return int(np.argmin(face_distances))