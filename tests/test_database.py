from smart_door_lock.database import log_access


def test_log_access_creates_csv_file(tmp_path):
    file_path = tmp_path / "attendance.csv"

    log_access("MOURAD", "AUTHORIZED", str(file_path))

    content = file_path.read_text(encoding="utf-8")

    assert "name,status,time" in content
    assert "MOURAD,AUTHORIZED" in content


def test_log_access_appends_refused_access(tmp_path):
    file_path = tmp_path / "attendance.csv"

    log_access("UNKNOWN", "REFUSED", str(file_path))

    content = file_path.read_text(encoding="utf-8")

    assert "UNKNOWN,REFUSED" in content