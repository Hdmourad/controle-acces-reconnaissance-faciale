from smart_door_lock.face_repository import (
    extract_person_name_from_file,
    is_supported_image_file,
    list_known_face_files,
    load_known_face_names,
)


def test_is_supported_image_file_accepts_valid_extensions():
    assert is_supported_image_file("Mourad.jpg") is True
    assert is_supported_image_file("Mourad.jpeg") is True
    assert is_supported_image_file("Mourad.png") is True


def test_is_supported_image_file_refuses_invalid_extensions():
    assert is_supported_image_file("notes.txt") is False
    assert is_supported_image_file("archive.zip") is False


def test_extract_person_name_from_file():
    result = extract_person_name_from_file("data/known_faces/Mourad_Hadji.jpg")

    assert result == "Mourad Hadji"


def test_list_known_face_files_returns_only_images(tmp_path):
    (tmp_path / "Mourad_Hadji.jpg").write_text("fake image")
    (tmp_path / "Adam.png").write_text("fake image")
    (tmp_path / "notes.txt").write_text("not an image")

    files = list_known_face_files(tmp_path)

    assert len(files) == 2
    assert files[0].name == "Adam.png"
    assert files[1].name == "Mourad_Hadji.jpg"


def test_load_known_face_names(tmp_path):
    (tmp_path / "Mourad_Hadji.jpg").write_text("fake image")
    (tmp_path / "Adam.png").write_text("fake image")

    names = load_known_face_names(tmp_path)

    assert names == ["Adam", "Mourad Hadji"]


def test_list_known_face_files_returns_empty_list_when_directory_missing(tmp_path):
    missing_directory = tmp_path / "missing"

    assert list_known_face_files(missing_directory) == []