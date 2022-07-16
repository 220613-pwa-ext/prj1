from flask import Blueprint, request, jsonify
from exception.Unauthorized import Unauthorized
from service.auth_service import AuthService
from flask_jwt_extended import create_access_token

ac = Blueprint('auth_controller', __name__)
auth_service = AuthService()


@ac.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        user = auth_service.login(username, password)
        access_token = create_access_token(identity={"user_id": user.get_user_id(),
                                                     "username": user.get_username(),
                                                     "first_name": user.get_first_name(),
                                                     "last_name": user.get_last_name(),
                                                     "email": user.get_email(),
                                                     "user_role": user.get_user_role()})
        return jsonify(access_token=access_token)
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401
