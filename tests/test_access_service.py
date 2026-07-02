from smart_door_lock.access_service import handle_access_request


class FakeLockController:
    def __init__(self):
        self.open_count = 0

    def open_lock(self):
        self.open_count += 1


def test_handle_access_request_authorizes_known_user():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = handle_access_request(
        name="mourad",
        distance=0.42,
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "MOURAD"
    assert result["status"] == "AUTHORIZED"
    assert result["opened"] is True
    assert lock.open_count == 1
    assert logs == [("MOURAD", "AUTHORIZED")]


def test_handle_access_request_refuses_unknown_user():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = handle_access_request(
        name=None,
        distance=None,
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "UNKNOWN"
    assert result["status"] == "REFUSED"
    assert result["opened"] is False
    assert lock.open_count == 0
    assert logs == [("UNKNOWN", "REFUSED")]


def test_handle_access_request_refuses_high_distance():
    lock = FakeLockController()
    logs = []

    def fake_logger(name, status):
        logs.append((name, status))

    result = handle_access_request(
        name="mourad",
        distance=0.80,
        lock_controller=lock,
        logger=fake_logger,
    )

    assert result["name"] == "UNKNOWN"
    assert result["status"] == "REFUSED"
    assert result["opened"] is False
    assert lock.open_count == 0
    assert logs == [("UNKNOWN", "REFUSED")]