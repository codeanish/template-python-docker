# template-python-docker

This repository is intended to be a starting off point for building a flask app inside a docker container and being able to execute tests locally before building the container. 

## Getting started

Check out the project and have a look around. From the root directory, issue a pipenv install to ensure that you pick up all the dependencies. Then ensure you can run the tests by typing pytest in the root directory of the virtual environment shell. Assuming you can do this, try running a docker build. Assuming the docker build is successful, run the container using the following command:

```docker run --rm -d -p 5000:5000  template-python-docker:latest```

 Ensure that you get a "Hello World" message from http://localhost:5000. If this all works, you're good.
 
 ## Tests
 
The Unit tests are unit tests, nothing magical here. This project is using pytest-docker to automate the building/tearing down of docker containers for the purposes of integration tests. Details on this package can be found here https://github.com/avast/pytest-docker.
 
The key bits are:
* /tests/docker-compose.yml residing in the /tests directory which lays out how to bring up the app for testing
* /tests/integration/conftest.py with the http_service fixture that is then available in all integration tests
* Each integration test needs to use the fixture http_service e.g. ```def test_hello_world(http_service: str)```
