from flask import Blueprint, request
from exception.UserNotFound import UserNotFound
from service.reimb_service import ReimbService

rc = Blueprint('reimb_controller', __name__)
reimb_service = ReimbService()

@rc.route('/users/<user_id>/reimbursements')
def get_all_reimb_by_user_id(user_id):
    try:
        return {"reimbursements": reimb_service.get_all_reimbursements_by_user_id(user_id)}, 200
    except UserNotFound as e:
        return {
               "message": str(e)
           }, 404