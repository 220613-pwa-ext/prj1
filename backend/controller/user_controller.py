from flask import Blueprint, request, jsonify
from exception.UserNotFound import UserNotFound
from service.user_service import UserService
from flask_jwt_extended import get_jwt_identity, jwt_required

uc = Blueprint('user_controller', __name__)
user_service = UserService()

@uc.route('/users')
@jwt_required()
def get_all_users():
    try:
        return {"users": user_service.get_all_users(), "requester": get_jwt_identity()}, 200
    except UserNotFound as e:
        return {
               "message": str(e)
           }, 404