from app import fetch_status


def test_fetch_status():
    assert callable(fetch_status)
