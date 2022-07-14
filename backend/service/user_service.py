from dao.user_dao import UserDao

class UserService:

    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self):

        return list(map(lambda x: x.to_dict(), self.user_dao.get_all_users()))

