from flask import Flask, jsonify
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from controller.reimb_controller import rc
from controller.user_controller import uc
from controller.auth_controller import ac
from dotenv import dotenv_values
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

config = dotenv_values(".env")






if __name__ == '__main__':
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = config.get('JWT_SECRET_KEY')
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "X-CSRF-TOKEN-ACCESS"
    app.config["JWT_REFRESH_CSRF_HEADER_NAME"] = "X-CSRF-TOKEN-REFRESH"
    jwt = JWTManager(app)
    app.register_blueprint(rc)
    app.register_blueprint(uc)
    app.register_blueprint(ac)
    # CORS(app)
    CORS(app, supports_credentials=True)


    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original response
            return response

    app.run(port=8080, debug=True)
