# template-python-docker

This repository is intended to be a starting off point for building a flask app inside a docker container and being able to execute tests locally before building the container. 

## Getting started

Check out the project and have a look around. From the root directory, issue a pipenv install to ensure that you pick up all the dependencies. Then ensure you can run the tests by typing pytest in the root directory of the virtual environment shell. Assuming you can do this, try running a docker build. Assuming the docker build is successful, run the container using the following command:

```docker run --rm -d -p 5000:5000  template-python-docker:latest```

 Ensure that you get a "Hello World" message from http://localhost:5000. If this all works, you're good.