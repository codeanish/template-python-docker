import pytest
import requests

from requests.exceptions import ConnectionError

def is_responsive(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):
    port = docker_services.port_for("app", 5000)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


def test_hello_world(http_service: str):
    response = requests.get(http_service)
    assert response.text == "Hello World"

def test_answer_to_the_meaning_of_life(http_service: str):
    response = requests.get(f"{http_service}/answer")
    assert response.text == "42"