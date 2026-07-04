from smart_door_lock.face_recognition_adapter import (
    compute_face_distances,
    extract_face_encodings,
    load_image,
)


class FakeFaceRecognitionBackend:
    def load_image_file(self, image_path):
        return f"image:{image_path}"

    def face_encodings(self, image):
        return [f"encoding:{image}"]

    def face_distance(self, known_encodings, detected_encoding):
        return [0.42, 0.80]


def test_load_image_uses_backend():
    backend = FakeFaceRecognitionBackend()

    image = load_image("Mourad.jpg", face_recognition_backend=backend)

    assert image == "image:Mourad.jpg"


def test_extract_face_encodings_uses_backend():
    backend = FakeFaceRecognitionBackend()

    encodings = extract_face_encodings("fake-image", face_recognition_backend=backend)

    assert encodings == ["encoding:fake-image"]


def test_compute_face_distances_uses_backend():
    backend = FakeFaceRecognitionBackend()

    distances = compute_face_distances(
        ["known-1", "known-2"],
        "detected",
        face_recognition_backend=backend,
    )

    assert distances == [0.42, 0.80]