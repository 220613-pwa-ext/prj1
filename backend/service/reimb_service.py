from dao.reimb_dao import ReimbDao
from dao.user_dao import UserDao
from exception.Unauthorized import Unauthorized


class ReimbService:

    def __init__(self):
        self.reimb_dao = ReimbDao()
        self.user_dao = UserDao()

    def get_reimbursements(self, req_id):
        user = self.user_dao.get_user_by_username(req_id.get('username'))
        if not user:
            raise Unauthorized('Login required')
        if user.get_user_role() == 1:
            print(user.get_user_role())
            return self.reimb_dao.get_all_reimb(req_id)
        else:
            return list(map(lambda x: x.to_dict(), self.reimb_dao.get_reimb_author_id(req_id)))

