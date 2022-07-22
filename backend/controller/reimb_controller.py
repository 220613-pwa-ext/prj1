import flask
from flask import Blueprint, request, make_response
from flask_cors import cross_origin

from exception.Unauthorized import Unauthorized
from exception.InvalidParameter import InvalidParameter
from exception.Forbidden import Forbidden
from service.reimb_service import ReimbService
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.datastructures import ImmutableMultiDict

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
    print(request.headers)
    if request.method == "OPTIONS":
        resp = flask.Response("preflight")
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Content-Length"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, OPTIONS, DELETE"
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp


    print(request.form)
    print(request.files)

    # amount = request.json.get("amount", None)
    # description = request.json.get("description", None)
    # receipt = request.json.get("receipt", None)
    # type_id = request.json.get("type_id", None)
    req_id = get_jwt_identity()
    try:
        # resolve = reimb_service.add_reimbursement(req_id, amount, description, receipt, type_id)
        return {"reimbursements": [], #reimb_service.get_reimbursements_by_user_id(req_id, None),
                "user": req_id.get('first_name'),
                "role": req_id.get('user_role'),
                "message": f"Request resolve status: {True}"}, 201
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


@rc.route('/handle-reimbursements/<reimbursement_id>')
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
