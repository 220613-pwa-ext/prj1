from dao.reimb_dao import ReimbDao


class ReimbService:

    def __init__(self):
        self.reimb_dao = ReimbDao()

    def get_all_reimbursements_by_user_id(self, user_id):

        return list(map(lambda x: x.to_dict(), self.reimb_dao.get_all_reimb_by_employee_id(user_id)))

