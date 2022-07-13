from flask import Flask
from controller.reimb_controller import rc

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(rc)
    app.run(port=8080, debug=True)
