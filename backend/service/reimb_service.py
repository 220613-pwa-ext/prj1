from dao.reimb_dao import UserDao

class ReimbService:

    def __init__(self):
        self.user_dao = UserDao()

    def get_all_reimbursements_by_user_id(self, user_id):

        return list(map(lambda x: x.to_dict(), self.user_dao.get_all_reimb_by_employee_id(user_id)))

