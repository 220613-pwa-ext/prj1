from dao.user_dao import UserDao
from exception.Forbidden import Forbidden

class UserService:

    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self, user):
        role = user.get('user_role')
        if role == 1 or role == 2:
            raise Forbidden('Forbidden resource access request!')
        elif role == 3:
            return list(map(lambda x: x.to_dict(), self.user_dao.get_all_users()))



