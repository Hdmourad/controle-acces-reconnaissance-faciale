from smart_door_lock.recognition import get_best_match_index, identify_face


def test_get_best_match_index_returns_lowest_distance_index():
    distances = [0.80, 0.42, 0.67]

    result = get_best_match_index(distances)

    assert result == 1


def test_get_best_match_index_returns_none_when_empty():
    assert get_best_match_index([]) is None


def test_identify_face_returns_known_user_when_distance_is_low():
    known_names = ["Bill Gates", "Mourad Hadji", "Jack Ma"]
    distances = [0.80, 0.42, 0.67]

    result = identify_face(known_names, distances)

    assert result["name"] == "MOURAD HADJI"
    assert result["matched"] is True
    assert result["distance"] == 0.42


def test_identify_face_refuses_when_distance_is_high():
    known_names = ["Bill Gates", "Mourad Hadji", "Jack Ma"]
    distances = [0.80, 0.72, 0.67]

    result = identify_face(known_names, distances)

    assert result["name"] is None
    assert result["matched"] is False
    assert result["distance"] == 0.67


def test_identify_face_returns_no_match_when_lists_are_empty():
    result = identify_face([], [])

    assert result["name"] is None
    assert result["distance"] is None
    assert result["matched"] is False