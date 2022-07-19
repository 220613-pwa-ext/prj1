from dao.reimb_dao import ReimbDao
from dao.user_dao import UserDao
from exception.Forbidden import Forbidden
from exception.Unauthorized import Unauthorized


class ReimbService:

    def __init__(self):
        self.reimb_dao = ReimbDao()
        self.user_dao = UserDao()

    def get_all_reimbursements(self, req_id):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        if not user:
            raise Unauthorized('Login required')
        elif user.get('user_role') == 1:
            return self.reimb_dao.get_all_reimb(req_id)
        else:
            raise Forbidden('Invalid authorization for the requested resource')


    def get_reimbursements_by_user_id(self, req_id):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        if not user:
            raise Unauthorized('Login required')
        else:
            return self.reimb_dao.get_reimb_author_id(req_id)
