import flask
from app import other_module

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return other_module.super_secret_message("World")

if __name__ == "__main__":
    app.run(host='0.0.0.0')