from dao.user_dao import UserDao
from exception.Unauthorized import Unauthorized
from exception.Forbidden import Forbidden
from utility.helpers import validate_password


class AuthService:

    def __init__(self):
        self.user_dao = UserDao()

    def login(self, username, password):
        user = self.user_dao.get_user_by_username(username)
        if not user:
            raise Unauthorized('Invalid username and/or password combination')
        if not validate_password(password, user.get_password()):
            raise Unauthorized('Invalid username and/or password combination')
        return user
