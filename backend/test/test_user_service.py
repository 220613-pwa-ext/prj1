import pytest

from controller.user_controller import user_service
from exception.Forbidden import Forbidden
from model.user import User


def test_get_all_users(mocker):
    #  Arrange
    def mock_get_all_users(self):
        returned_records = [
            (1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'John', 'Doe', 'jd@a.ca', 2),
            (2, 'JaneD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Jane', 'Doe', 'jd@a.ca', 2),
            (3, 'JonD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Johny', 'Doe', 'jd@a.ca', 3),
            (4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin', 'Vlad', 'vv@a.ca',
             1),
            (5, 'willrock22', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Cam', 'Coder', 'jd@a.ca',
             1)]
        res = []
        for record in returned_records:
            print(record)
            res.append(User(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
        return res

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_get_all_users)
    # Act
    actual = user_service.get_all_users({'first_name': 'Johny', 'user_role': 3})

    # Assert
    assert actual == [
        {'user_id': 1,
         'username': 'JohnD80',
         'password': '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
         'first_name': 'John',
         'last_name': 'Doe',
         'email': 'jd@a.ca',
         'user_role': 2
         },
        {'user_id': 2,
         'username': 'JaneD80',
         'password': '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
         'first_name': 'Jane',
         'last_name': 'Doe',
         'email': 'jd@a.ca',
         'user_role': 2
         },
        {'user_id': 3,
         'username': 'JonD80',
         'password': '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
         'first_name': 'Johny',
         'last_name': 'Doe',
         'email': 'jd@a.ca',
         'user_role': 3
         },
        {'user_id': 4,
         'username': 'valiv9',
         'password': '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
         'first_name': 'Valentin',
         'last_name': 'Vlad',
         'email': 'vv@a.ca',
         'user_role': 1
         },
        {'user_id': 5,
         'username': 'willrock22',
         'password': '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
         'first_name': 'Cam',
         'last_name': 'Coder',
         'email': 'jd@a.ca',
         'user_role': 1
         }]


def test_get_all_users_invalid_role(mocker):
    #  Arrange
    def mock_get_all_users(self):
        returned_records = [
            (1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'John', 'Doe', 'jd@a.ca', 2),
            (2, 'JaneD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Jane', 'Doe', 'jd@a.ca', 2),
            (3, 'JonD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Johny', 'Doe', 'jd@a.ca', 3),
            (4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin', 'Vlad', 'vv@a.ca',
             1),
            (5, 'willrock22', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Cam', 'Coder', 'jd@a.ca',
             1)]
        res = []
        for record in returned_records:
            print(record)
            res.append(User(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
        return res

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_get_all_users)

    # Act and  # Assert
    with pytest.raises(Forbidden):
        user_service.get_all_users({'first_name': 'Valentin', 'user_role': 1})
