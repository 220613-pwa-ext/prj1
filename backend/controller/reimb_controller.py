from flask import Blueprint, request
from exception.UserNotFound import UserNotFound

cc = Blueprint('customer_controller', __name__)

@cc.route('/users/<user_id>/reimbursements')
def get_all_reimb_by_user_id(user_id):
    try:
        return 'test', 200
    except UserNotFound as e:
        return {
               "message": str(e)
           }, 404