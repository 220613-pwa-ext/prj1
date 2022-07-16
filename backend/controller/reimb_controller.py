from flask import Blueprint, request
from exception.Unauthorized import Unauthorized
from service.reimb_service import ReimbService
from flask_jwt_extended import get_jwt_identity, jwt_required

rc = Blueprint('reimb_controller', __name__)
reimb_service = ReimbService()

@rc.route('/reimbursements')
@jwt_required()
def get_reimbursements():
    req_id = get_jwt_identity()
    try:
        return {"reimbursements": reimb_service.get_reimbursements(req_id)}, 200
    except Unauthorized as e:
        return {
               "message": str(e)
           }, 401