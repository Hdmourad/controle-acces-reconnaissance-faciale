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


def identify_face(known_names, face_distances, threshold: float = 0.55):
    """
    Identifie une personne à partir des distances faciales.

    known_names : liste des noms connus
    face_distances : liste des distances calculées
    threshold : seuil maximal accepté pour autoriser la reconnaissance

    Retourne :
    - le nom reconnu
    - la distance
    - l'état matched True/False
    """
    if len(known_names) == 0 or len(face_distances) == 0:
        return {
            "name": None,
            "distance": None,
            "matched": False,
        }

    match_index = get_best_match_index(face_distances)
    best_distance = float(face_distances[match_index])

    if best_distance < threshold:
        return {
            "name": known_names[match_index].upper(),
            "distance": best_distance,
            "matched": True,
        }

    return {
        "name": None,
        "distance": best_distance,
        "matched": False,
    }