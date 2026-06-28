from smart_door_lock.access_control import is_access_authorized


def test_access_authorized_when_distance_is_low():
    assert is_access_authorized(0.42) is True


def test_access_refused_when_distance_is_high():
    assert is_access_authorized(0.80) is False


def test_access_refused_when_distance_equal_threshold():
    assert is_access_authorized(0.55) is False