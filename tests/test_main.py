from smart_door_lock.main import run_demo_access


def test_run_demo_access_authorizes_demo_user():
    result = run_demo_access()

    assert result["name"] == "MOURAD HADJI"
    assert result["status"] == "AUTHORIZED"
    assert result["opened"] is True