from flask import Blueprint, request, jsonify
from exception.UserNotFound import UserNotFound
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
        role = auth_service.login(username, password)
        access_token = create_access_token(identity={"username": username, 'role': role})
        return jsonify(access_token=access_token)
    except UserNotFound as e:
        return {
               "message": str(e)
           }, 404
    except Unauthorized as e:
        return {
               "message": str(e)
           }, 401
