import flask
from app import other_module

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return other_module.super_secret_message("World")


@app.route('/answer', methods=['GET'])
def answer_to_the_ultimate_question_of_life():
    return "42"

if __name__ == "__main__":
    app.run(host='0.0.0.0')