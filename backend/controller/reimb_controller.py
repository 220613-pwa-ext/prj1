import flask
from flask import Blueprint, request
from exception.Unauthorized import Unauthorized
from exception.InvalidParameter import InvalidParameter
from exception.Forbidden import Forbidden
from service.reimb_service import ReimbService
from flask_jwt_extended import get_jwt_identity, jwt_required

rc = Blueprint('reimb_controller', __name__)
reimb_service = ReimbService()


@rc.route('/reimbursements')
@jwt_required()
def get_reimbursements():
    args = request.args
    req_id = get_jwt_identity()
    try:
        return {"reimbursements": reimb_service.get_reimbursements_by_user_id(req_id, args),
                "user": req_id.get('first_name'),
                "role": req_id.get('user_role')}, 200
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400
    except Forbidden as e:
        return {
                   "message": str(e)
               }, 403


@rc.route('/reimbursement', methods=['POST', 'OPTIONS'])
@jwt_required()
def add_reimbursement():
    if request.method == "OPTIONS":
        resp = flask.Response("preflight")
        resp.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Content-Length"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp

    elif request.method == "POST":
        print(request.form)
        print(request.files)
        amount = request.form.get("amount", None)
        description = request.form.get("description", None)
        receipt = request.files['receipt']
        print(receipt)
        type_id = request.form.get("type_id", None)
        req_id = get_jwt_identity()
        try:
            resolve = reimb_service.add_reimbursement(req_id, amount, description, receipt, type_id)
            new_data = reimb_service.get_reimbursements_by_user_id(req_id, None)
            print(new_data)
            return {"reimbursements": new_data,
                    "user": req_id.get('first_name'),
                    "role": req_id.get('user_role'),
                    "message": f"Request resolve status: {resolve}"}, 201
        except Unauthorized as e:
            return {
                       "message": str(e)
                   }, 401
        except InvalidParameter as e:
            return {
                       "message": str(e)
                   }, 400
        except Forbidden as e:
            return {
                       "message": str(e)
                   }, 403


@rc.route('/handle-reimbursements')
@jwt_required()
def get_all_reimbursements_by_user_id():
    args = request.args
    req_id = get_jwt_identity()
    try:
        return {"reimbursements": reimb_service.get_all_reimbursements(req_id, args),
                "user": req_id.get('first_name'),
                "role": req_id.get('user_role')}, 200
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401


@rc.route('/handle-reimbursements/<reimbursement_id>', methods=['PUT'])
@jwt_required()
def update_reimbursement_by_reimb_id(reimbursement_id):
    status = int(str(reimbursement_id)[0])
    reimb_id = int(str(reimbursement_id)[1:])
    print(status, " ", reimb_id)
    req_id = get_jwt_identity()

    try:
        reimb_service.update_reimbursement_by_reimb_id(req_id, reimb_id, status)
        return {"reimbursements": reimb_service.get_all_reimbursements(req_id, None),
                "user": req_id.get('first_name'),
                "role": req_id.get('user_role')}, 201
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400
    except Forbidden as e:
        return {
                   "message": str(e)
               }, 403
