import requests

def test_hello_world(http_service: str):
    response = requests.get(http_service)
    assert response.text == "Hello World"

def test_answer_to_the_meaning_of_life(http_service: str):
    response = requests.get(f"{http_service}/answer")
    assert response.text == "42"