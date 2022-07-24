from dao.reimb_dao import ReimbDao
from dao.user_dao import UserDao
from exception.Forbidden import Forbidden
from exception.Unauthorized import Unauthorized
from exception.InvalidParameter import InvalidParameter

class ReimbService:

    def __init__(self):
        self.reimb_dao = ReimbDao()
        self.user_dao = UserDao()

    def get_all_reimbursements(self, req_id, args):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        if not user:
            raise Unauthorized('Login required')
        elif user.get_user_role() > 1:
            raise Forbidden('Invalid authorization for the requested resource')
        elif not args or int(args.get('status')) == 0:
            return self.reimb_dao.get_all_reimb(req_id)
        elif int(args.get('status')) in (1, 2, 3):
            return self.reimb_dao.get_all_reimb_args(req_id, args)




    def get_reimbursements_by_user_id(self, req_id, args):
        user = self.user_dao.get_user_by_username(req_id.get('username'))

        if not user:
            raise Unauthorized('Login required')
        if not args or int(args.get('status')) == 0:
            return self.reimb_dao.get_reimb_author_id(req_id)
        elif int(args.get('status')) not in (1, 2, 3):
            raise InvalidParameter('Expected query parameter name was "status" with the value 1, 2, or 3!')
        else:
            return self.reimb_dao.get_reimb_author_id_args(req_id, args)

    def update_reimbursement_by_reimb_id(self, req_id, reimb_id, status):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        reimb = self.reimb_dao.get_reimb_by_reimb_id(reimb_id)
        if not user:
            raise Unauthorized('Login required')
        elif user.get_user_role() > 1:
            raise Forbidden('Invalid authorization for the requested resource')
        elif reimb.get_status_id() != 1:
            raise Forbidden('The requested resource is in a resolved status already')
        elif status not in (2, 3):
            raise InvalidParameter('The allowed values are either 3 or 2!')
        elif self.reimb_dao.update_reimb_by_reimb_id(reimb_id, req_id.get('user_id'), status):
            return "Successful data update!"

    def add_reimbursement(self, req_id, amount, description, receipt, type_id):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        if not user:
            raise Unauthorized('Login required')
        try:
            amount = float(amount)
            type_id = float(type_id)
        except ValueError as e:
            raise InvalidParameter('Enter numbers for this field')
        return self.reimb_dao.add_reimb(req_id, amount, description, type_id, receipt)



