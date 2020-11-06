from app import api

def test_health_check():
    assert api.health_check() == "Hello World"