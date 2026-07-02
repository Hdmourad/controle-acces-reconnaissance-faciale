from smart_door_lock.recognition import get_best_match_index


def test_get_best_match_index_returns_lowest_distance_index():
    distances = [0.80, 0.42, 0.67]

    result = get_best_match_index(distances)

    assert result == 1


def test_get_best_match_index_returns_none_when_empty():
    assert get_best_match_index([]) is None