from smart_door_lock.workflow import process_face_access


class FakeLockController:
    def __init__(self):
        self.open_count = 0

    def open_lock(self):
        self.open_count += 1


def test_process_face_access_authorizes_best_match():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = process_face_access(
        known_names=["Bill Gates", "Mourad Hadji", "Jack Ma"],
        face_distances=[0.80, 0.42, 0.67],
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "MOURAD HADJI"
    assert result["status"] == "AUTHORIZED"
    assert result["opened"] is True
    assert lock.open_count == 1
    assert logs == [("MOURAD HADJI", "AUTHORIZED")]


def test_process_face_access_refuses_unknown_face():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = process_face_access(
        known_names=["Bill Gates", "Mourad Hadji", "Jack Ma"],
        face_distances=[0.80, 0.72, 0.67],
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "UNKNOWN"
    assert result["status"] == "REFUSED"
    assert result["opened"] is False
    assert lock.open_count == 0
    assert logs == [("UNKNOWN", "REFUSED")]


def test_process_face_access_refuses_when_no_known_faces():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = process_face_access(
        known_names=[],
        face_distances=[],
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "UNKNOWN"
    assert result["status"] == "REFUSED"
    assert result["opened"] is False
    assert lock.open_count == 0
    assert logs == [("UNKNOWN", "REFUSED")]