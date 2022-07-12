from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)

    app.run(port=8080, debug=True)
