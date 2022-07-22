from flask import Blueprint, request, jsonify, make_response
from exception.Unauthorized import Unauthorized
from service.auth_service import AuthService
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from flask_cors import cross_origin

ac = Blueprint('auth_controller', __name__)
auth_service = AuthService()


@ac.route('/login', methods=['POST', 'OPTIONS'])
# @cross_origin(supports_credentials=True)
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        user = auth_service.login(username, password)
        response = jsonify({"msg": "login successful"})
        # response.headers['Access-Control-Allow-Credentials'] = ''
        access_token = create_access_token(identity={"user_id": user.get_user_id(),
                                                     "username": user.get_username(),
                                                     "first_name": user.get_first_name(),
                                                     "last_name": user.get_last_name(),
                                                     "email": user.get_email(),
                                                     "user_role": user.get_user_role()})
        set_access_cookies(response, access_token)

        return response
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401


@ac.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
