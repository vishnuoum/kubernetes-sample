from flask import Flask, Response
from http import HTTPStatus

app = Flask(__name__)


@app.get("/")
def greet():
    return Response("Hello world", status=HTTPStatus.OK)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)