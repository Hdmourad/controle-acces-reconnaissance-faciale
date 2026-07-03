from smart_door_lock import config


def test_face_distance_threshold_is_valid():
    assert 0 < config.FACE_DISTANCE_THRESHOLD < 1


def test_gpio_lock_pin_is_gpio17():
    assert config.GPIO_LOCK_PIN == 17


def test_lock_open_duration_is_positive():
    assert config.LOCK_OPEN_DURATION_SECONDS > 0


def test_known_faces_directory_is_configured():
    assert config.KNOWN_FACES_DIR == "data/known_faces"


def test_allowed_image_extensions_are_defined():
    assert ".jpg" in config.ALLOWED_IMAGE_EXTENSIONS
    assert ".jpeg" in config.ALLOWED_IMAGE_EXTENSIONS
    assert ".png" in config.ALLOWED_IMAGE_EXTENSIONS