from flask import Blueprint, request
from exception.UserNotFound import UserNotFound
from service.user_service import UserService

uc = Blueprint('user_controller', __name__)
user_service = UserService()

@uc.route('/users')
def get_all_users():
    try:
        return {"users": user_service.get_all_users()}, 200
    except UserNotFound as e:
        return {
               "message": str(e)
           }, 404