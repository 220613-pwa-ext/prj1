from flask import Flask
from controller.reimb_controller import rc
from controller.user_controller import uc
from controller.auth_controller import ac
from dotenv import dotenv_values
from flask_jwt_extended import JWTManager
from flask_cors import CORS

config = dotenv_values(".env")

if __name__ == '__main__':
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = config.get('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    app.register_blueprint(rc)
    app.register_blueprint(uc)
    app.register_blueprint(ac)
    CORS(app)
    app.run(port=8080, debug=True)
