from smart_door_lock.face_encoding import (
    build_known_face_encoding,
    encode_face_with_backend,
    load_image_with_backend,
)


def test_load_image_with_backend_calls_loader():
    calls = []

    def fake_loader(path):
        calls.append(path)
        return "fake-image"

    image = load_image_with_backend("data/known_faces/Mourad.jpg", fake_loader)

    assert image == "fake-image"
    assert calls == ["data/known_faces/Mourad.jpg"]


def test_encode_face_with_backend_returns_first_encoding():
    def fake_encoder(image):
        return ["encoding-1", "encoding-2"]

    result = encode_face_with_backend("fake-image", fake_encoder)

    assert result == "encoding-1"


def test_encode_face_with_backend_returns_none_when_no_face_detected():
    def fake_encoder(image):
        return []

    result = encode_face_with_backend("fake-image", fake_encoder)

    assert result is None


def test_build_known_face_encoding_loads_and_encodes_image():
    def fake_loader(path):
        return f"image-loaded-from-{path}"

    def fake_encoder(image):
        return [f"encoding-of-{image}"]

    result = build_known_face_encoding(
        "Mourad.jpg",
        image_loader=fake_loader,
        face_encoder=fake_encoder,
    )

    assert result == "encoding-of-image-loaded-from-Mourad.jpg"