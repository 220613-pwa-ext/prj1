class User:
    def __init__(self,
                 user_id,
                 username,
                 password,
                 first_name,
                 last_name,
                 email,
                 user_role,
                 ):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__user_role = user_role
        self.__username = username
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_user_role(self):
        return self.__user_role

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_first_name(self, value):
        self.__first_name = value

    def set_user_id(self, value):
        self.__user_id = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_email(self, value):
        self.__email = value

    def set_user_role(self, value):
        self.__user_role = value

    def set_username(self, value):
        self.__username = value

    def set_password(self, value):
        self.__password = value

    def to_dict(self):
        return {
            'user_id': self.get_user_id(),
            'username': self.get_username(),
            'password': self.get_password(),
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'email': self.get_email(),
            'user_role': self.get_user_role()
        }

    def __str__(self):
        return "User(id='%s')" % self.get_user_id()
