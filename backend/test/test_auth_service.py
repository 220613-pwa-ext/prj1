import pytest

from controller.auth_controller import auth_service
from exception.Unauthorized import Unauthorized
from model.user import User


def test_login_valid_username_valid_password(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        record = (1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                            'John', 'Doe', 'jd@a.ca', 2)
        if record:
            return User(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    # Act
    actual = auth_service.login('JohnD80', 'password')

    # Assert
    assert (actual.get_username() == User(1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                            'John', 'Doe', 'jd@a.ca', 2).get_username() and
            actual.get_password() == User(1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                                          'John', 'Doe', 'jd@a.ca', 2).get_password()
            )


def test_login_valid_username_invalid_password(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        record = (1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                            'John', 'Doe', 'jd@a.ca', 2)
        if record:
            return User(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    # Act and  # Assert
    with pytest.raises(Unauthorized):
        auth_service.login('valiv9', 'bec')

def test_login_invalid_username_valid_password(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        record = None
        if record:
            return User(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    # Act and  # Assert
    with pytest.raises(Unauthorized):
        auth_service.login('logo', 'password')

def test_login_invalid_username_invalid_password(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        record = None
        if record:
            return User(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    # Act and  # Assert
    with pytest.raises(Unauthorized):
        auth_service.login('logo', 'bec')