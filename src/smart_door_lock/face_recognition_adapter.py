def load_image(image_path: str, face_recognition_backend=None):
    """
    Charge une image avec la bibliothèque face_recognition.
    """
    if face_recognition_backend is None:
        import face_recognition as face_recognition_backend

    return face_recognition_backend.load_image_file(image_path)


def extract_face_encodings(image, face_recognition_backend=None):
    """
    Extrait les encodages faciaux depuis une image.
    """
    if face_recognition_backend is None:
        import face_recognition as face_recognition_backend

    return face_recognition_backend.face_encodings(image)


def compute_face_distances(known_encodings, detected_encoding, face_recognition_backend=None):
    """
    Calcule les distances entre les visages connus et le visage détecté.
    """
    if face_recognition_backend is None:
        import face_recognition as face_recognition_backend

    return face_recognition_backend.face_distance(known_encodings, detected_encoding)