from flask import Blueprint, request, jsonify
from exception.Forbidden import Forbidden
from service.user_service import UserService
from flask_jwt_extended import get_jwt_identity, jwt_required

uc = Blueprint('user_controller', __name__)
user_service = UserService()

@uc.route('/users')
@jwt_required()
def get_all_users():
    user = get_jwt_identity()
    try:
        return {"users": user_service.get_all_users(user), "first_name": user.get('first_name')}, 200
    except Forbidden as e:
        return {
               "message": str(e)
           }, 403
