from datetime import datetime
from decimal import Decimal

import pytest

from controller.reimb_controller import reimb_service
from exception.Forbidden import Forbidden
from exception.Unauthorized import Unauthorized
from exception.InvalidParameter import InvalidParameter
from model.reimbursement import Reimbursement
from model.user import User


def test_get_all_reimbursements_for_a_finance_manager_passing_invalid_user(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return None

    def mock_get_all_reimb_args(self, req_id, args):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'author': 'Valentin Vlad'},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 9, 'amount': Decimal('100'), 'submitted': datetime(2022, 7, 24, 11, 12, 28, 2219),
                 'status_name': 'approved', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/9.jpeg', 'author': 'John Doe'},
                {'r_id': 10, 'amount': Decimal('5'), 'submitted': datetime(2022, 7, 24, 11, 15, 48, 696540),
                 'status_name': 'approved', 'r_name': 'Other', 'description': 'Coffee interview',
                 'receipt': '/receipts/10.jpeg', 'author': 'John Doe'},
                {'r_id': 11, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 16, 28, 7197),
                 'status_name': 'denied', 'r_name': 'Lodging', 'description': 'Hotel - 1 night',
                 'receipt': '/receipts/11.jpeg', 'author': 'John Doe'},
                {'r_id': 12, 'amount': Decimal('30'), 'submitted': datetime(2022, 7, 24, 11, 18, 11, 284372),
                 'status_name': 'denied', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/12.jpeg',
                 'author': 'John Doe'},
                {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                 'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                 'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                 'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                 'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                 'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel', 'receipt': '/receipts/19.jpeg',
                 'author': 'John Doe'},
                {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                 'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_all_reimb_args', mock_get_all_reimb_args)

    # Act and  # Assert
    with pytest.raises(Unauthorized):
        reimb_service.get_all_reimbursements(
            {'user_id': 5, 'username': 'logo', 'first_name': 'Cam', 'last_name': 'Coder', 'email': 'jd@a.ca',
             'user_role': 1}, {'status': 0}
        )


def test_get_all_reimbursements_for_a_finance_manager_passing_employee(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(1, 'JohnD80', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'John', 'Doe',
                    'jd@a.ca', 2)

    def mock_get_all_reimb_args(self, req_id, args):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'author': 'Valentin Vlad'},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 9, 'amount': Decimal('100'), 'submitted': datetime(2022, 7, 24, 11, 12, 28, 2219),
                 'status_name': 'approved', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/9.jpeg', 'author': 'John Doe'},
                {'r_id': 10, 'amount': Decimal('5'), 'submitted': datetime(2022, 7, 24, 11, 15, 48, 696540),
                 'status_name': 'approved', 'r_name': 'Other', 'description': 'Coffee interview',
                 'receipt': '/receipts/10.jpeg', 'author': 'John Doe'},
                {'r_id': 11, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 16, 28, 7197),
                 'status_name': 'denied', 'r_name': 'Lodging', 'description': 'Hotel - 1 night',
                 'receipt': '/receipts/11.jpeg', 'author': 'John Doe'},
                {'r_id': 12, 'amount': Decimal('30'), 'submitted': datetime(2022, 7, 24, 11, 18, 11, 284372),
                 'status_name': 'denied', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/12.jpeg',
                 'author': 'John Doe'},
                {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                 'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                 'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                 'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                 'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                 'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel', 'receipt': '/receipts/19.jpeg',
                 'author': 'John Doe'},
                {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                 'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_all_reimb_args', mock_get_all_reimb_args)

    # Act and  # Assert
    with pytest.raises(Forbidden):
        reimb_service.get_all_reimbursements(
            {'user_id': 1, 'username': 'JohnD80', 'first_name': 'John', 'last_name': 'Doe', 'email': 'jd@a.ca',
             'user_role': 2}, {'status': 0}
        )


def test_get_all_reimbursements_for_a_finance_manager(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(5, 'willrock22', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                    'Cam', 'Coder', 'jd@a.ca', 1)

    def mock_get_all_reimb(self, req_id):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'author': 'Valentin Vlad'},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 9, 'amount': Decimal('100'), 'submitted': datetime(2022, 7, 24, 11, 12, 28, 2219),
                 'status_name': 'approved', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/9.jpeg', 'author': 'John Doe'},
                {'r_id': 10, 'amount': Decimal('5'), 'submitted': datetime(2022, 7, 24, 11, 15, 48, 696540),
                 'status_name': 'approved', 'r_name': 'Other', 'description': 'Coffee interview',
                 'receipt': '/receipts/10.jpeg', 'author': 'John Doe'},
                {'r_id': 11, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 16, 28, 7197),
                 'status_name': 'denied', 'r_name': 'Lodging', 'description': 'Hotel - 1 night',
                 'receipt': '/receipts/11.jpeg', 'author': 'John Doe'},
                {'r_id': 12, 'amount': Decimal('30'), 'submitted': datetime(2022, 7, 24, 11, 18, 11, 284372),
                 'status_name': 'denied', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/12.jpeg',
                 'author': 'John Doe'},
                {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                 'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                 'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                 'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                 'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                 'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel', 'receipt': '/receipts/19.jpeg',
                 'author': 'John Doe'},
                {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                 'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_all_reimb', mock_get_all_reimb)
    # Act
    actual = reimb_service.get_all_reimbursements(
        {'user_id': 5, 'username': 'willrock22', 'first_name': 'Cam', 'last_name': 'Coder', 'email': 'jd@a.ca',
         'user_role': 1}, {'status': 0}
    )

    # Assert
    assert actual == [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch',
                       'receipt': '/receipts/6.jpeg', 'author': 'Valentin Vlad'},
                      {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                       'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                      {'r_id': 9, 'amount': Decimal('100'), 'submitted': datetime(2022, 7, 24, 11, 12, 28, 2219),
                       'status_name': 'approved', 'r_name': 'Travel', 'description': 'Subway pass',
                       'receipt': '/receipts/9.jpeg', 'author': 'John Doe'},
                      {'r_id': 10, 'amount': Decimal('5'), 'submitted': datetime(2022, 7, 24, 11, 15, 48, 696540),
                       'status_name': 'approved', 'r_name': 'Other', 'description': 'Coffee interview',
                       'receipt': '/receipts/10.jpeg', 'author': 'John Doe'},
                      {'r_id': 11, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 16, 28, 7197),
                       'status_name': 'denied', 'r_name': 'Lodging', 'description': 'Hotel - 1 night',
                       'receipt': '/receipts/11.jpeg', 'author': 'John Doe'},
                      {'r_id': 12, 'amount': Decimal('30'), 'submitted': datetime(2022, 7, 24, 11, 18, 11, 284372),
                       'status_name': 'denied', 'r_name': 'Food', 'description': 'Lunch',
                       'receipt': '/receipts/12.jpeg', 'author': 'John Doe'},
                      {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                       'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                      {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                       'status_name': 'denied', 'r_name': 'Other',
                       'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                       'receipt': '/receipts/14.jpeg', 'author': 'Valentin Vlad'},
                      {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                       'status_name': 'approved', 'r_name': 'Lodging',
                       'description': 'Hotel - work related -two nights', 'receipt': '/receipts/15.jpeg',
                       'author': 'Valentin Vlad'},
                      {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                       'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                       'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                      {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                       'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                      {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                       'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel',
                       'receipt': '/receipts/19.jpeg', 'author': 'John Doe'},
                      {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                       'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                      {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                       'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]


def test_get_all_reimbursements_for_a_finance_manager_with_filter(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(5, 'willrock22', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2',
                    'Cam', 'Coder', 'jd@a.ca', 1)

    def mock_get_all_reimb_args(self, req_id, args):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch',
                 'receipt': '/receipts/6.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                 'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                 'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                 'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                 'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                 'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel',
                 'receipt': '/receipts/19.jpeg', 'author': 'John Doe'},
                {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                 'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_all_reimb_args', mock_get_all_reimb_args)
    # Act
    actual = reimb_service.get_all_reimbursements(
        {'user_id': 5, 'username': 'willrock22', 'first_name': 'Cam', 'last_name': 'Coder', 'email': 'jd@a.ca',
         'user_role': 1}, {'status': 1}
    )

    # Assert
    assert actual == [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch',
                       'receipt': '/receipts/6.jpeg', 'author': 'Valentin Vlad'},
                      {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                       'receipt': '/receipts/7.jpeg', 'author': 'Valentin Vlad'},
                      {'r_id': 13, 'amount': Decimal('40'), 'submitted': datetime(2022, 7, 24, 11, 19, 9, 383049),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Uber - late for work',
                       'receipt': '/receipts/13.jpeg', 'author': 'John Doe'},
                      {'r_id': 16, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 11, 59, 45, 923611),
                       'status_name': 'pending', 'r_name': 'Other', 'description': 'New suit - since promoted',
                       'receipt': '/receipts/16.jpeg', 'author': 'John Doe'},
                      {'r_id': 17, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 12, 0, 20, 628139),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Outrageous request',
                       'receipt': '/receipts/17.jpeg', 'author': 'John Doe'},
                      {'r_id': 19, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 14, 57, 51, 668624),
                       'status_name': 'pending', 'r_name': 'Lodging', 'description': 'Motel',
                       'receipt': '/receipts/19.jpeg', 'author': 'John Doe'},
                      {'r_id': 20, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 24, 15, 22, 59, 551157),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Manager',
                       'receipt': '/receipts/20.jpeg', 'author': 'John Doe'},
                      {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                       'receipt': '/receipts/21.jpeg', 'author': 'Valentin Vlad'}]


def test_get_reimbursements_by_user_id_for_an_employee(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_get_reimb_author_id(self, req_id):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'resolver': ' '},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'resolver': ' '}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb_author_id', mock_get_reimb_author_id)
    # Act
    actual = reimb_service.get_reimbursements_by_user_id(
        {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
         'user_role': 1}, {'status': 0}
    )

    # Assert
    assert actual == [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch',
                       'receipt': '/receipts/6.jpeg', 'resolver': ' '},
                      {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                       'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                      {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                       'status_name': 'denied', 'r_name': 'Other',
                       'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                       'receipt': '/receipts/14.jpeg', 'resolver': 'Cam Coder'},
                      {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                       'status_name': 'approved', 'r_name': 'Lodging',
                       'description': 'Hotel - work related -two nights', 'receipt': '/receipts/15.jpeg',
                       'resolver': 'Cam Coder'},
                      {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                       'receipt': '/receipts/21.jpeg', 'resolver': ' '}]


def test_get_reimbursements_by_user_id_for_an_invalid_user(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return None

    def mock_get_reimb_author_id(self, req_id):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'resolver': ' '},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'resolver': ' '}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb_author_id', mock_get_reimb_author_id)

    # Act and  # Assert
    with pytest.raises(Unauthorized):
        reimb_service.get_reimbursements_by_user_id(
            {'user_id': 1, 'username': 'logo', 'first_name': 'John', 'last_name': 'Doe', 'email': 'jd@a.ca',
             'user_role': 2}, {'status': 0}
        )


def test_get_reimbursements_by_user_id_for_an_employee_invalid_status_on_filter(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_get_reimb_author_id(self, req_id):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'resolver': ' '},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                {'r_id': 14, 'amount': Decimal('3000'), 'submitted': datetime(2022, 7, 24, 11, 42, 42, 210833),
                 'status_name': 'denied', 'r_name': 'Other',
                 'description': 'Bracelet - make peace with spouse for spending two nights for work purpose',
                 'receipt': '/receipts/14.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 15, 'amount': Decimal('500'), 'submitted': datetime(2022, 7, 24, 11, 43, 21, 70466),
                 'status_name': 'approved', 'r_name': 'Lodging', 'description': 'Hotel - work related -two nights',
                 'receipt': '/receipts/15.jpeg', 'resolver': 'Cam Coder'},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'resolver': ' '}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb_author_id', mock_get_reimb_author_id)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        reimb_service.get_reimbursements_by_user_id(
            {'user_id': 1, 'username': 'logo', 'first_name': 'John', 'last_name': 'Doe', 'email': 'jd@a.ca',
             'user_role': 2}, {'status': 7}
        )


def test_get_reimbursements_by_user_id_for_an_employee_with_filter(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_get_reimb_author_id_args(self, req_id, args):
        return [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                 'resolver': ' '},
                {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                 'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                 'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                 'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                 'receipt': '/receipts/21.jpeg', 'resolver': ' '}]

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb_author_id_args', mock_get_reimb_author_id_args)
    # Act
    actual = reimb_service.get_reimbursements_by_user_id(
        {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
         'user_role': 1}, {'status': 1}
    )

    # Assert
    assert actual == [{'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch',
                       'receipt': '/receipts/6.jpeg', 'resolver': ' '},
                      {'r_id': 7, 'amount': Decimal('700'), 'submitted': datetime(2022, 7, 24, 11, 0, 38, 366206),
                       'status_name': 'pending', 'r_name': 'Travel', 'description': 'Subway pass',
                       'receipt': '/receipts/7.jpeg', 'resolver': ' '},
                      {'r_id': 21, 'amount': Decimal('200'), 'submitted': datetime(2022, 7, 25, 10, 37, 9, 503602),
                       'status_name': 'pending', 'r_name': 'Food', 'description': 'Lunch with Project Manager',
                       'receipt': '/receipts/21.jpeg', 'resolver': ' '}]


def test_update_reimbursement_by_reimb_id_valid_fields(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_update_reimb_by_reimb_id(self, reimb_id, user_id, status):
        return 'Successful data update!'

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.update_reimb_by_reimb_id', mock_update_reimb_by_reimb_id)
    # Act
    actual = reimb_service.update_reimbursement_by_reimb_id(
        {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
         'user_role': 1}, 6, 2)

    # Assert
    assert actual == 'Successful data update!'


def test_update_reimbursement_by_reimb_id_invalid_status(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_update_reimb_by_reimb_id(self, reimb_id, user_id, status):
        return {'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                'status_name': 'approved', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                'resolver': ' '}

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.update_reimb_by_reimb_id', mock_update_reimb_by_reimb_id)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        reimb_service.update_reimbursement_by_reimb_id(
            {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 6, {'status': 1}
        )


def test_update_reimbursement_by_reimb_id_invalid_user(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return None

    def mock_update_reimb_by_reimb_id(self, reimb_id, user_id, status):
        return {'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                'status_name': 'approved', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                'resolver': ' '}

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.update_reimb_by_reimb_id', mock_update_reimb_by_reimb_id)

    # Act and  # Assert
    with pytest.raises(Unauthorized):
        reimb_service.update_reimbursement_by_reimb_id(
            {'user_id': 4, 'username': 'logo', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 6, {'status': 1}
        )


def test_update_reimbursement_by_reimb_id_invalid_role(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 2)

    def mock_update_reimb_by_reimb_id(self, reimb_id, user_id, status):
        return {'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                'status_name': 'approved', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                'resolver': ' '}

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.update_reimb_by_reimb_id', mock_update_reimb_by_reimb_id)

    # Act and  # Assert
    with pytest.raises(Forbidden):
        reimb_service.update_reimbursement_by_reimb_id(
            {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 6, {'status': 2}
        )


def test_update_reimbursement_by_reimb_id_invalid_current_status(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_update_reimb_by_reimb_id(self, reimb_id, user_id, status):
        return {'r_id': 6, 'amount': Decimal('400'), 'submitted': datetime(2022, 7, 24, 10, 58, 35, 454687),
                'status_name': 'approved', 'r_name': 'Food', 'description': 'Lunch', 'receipt': '/receipts/6.jpeg',
                'resolver': ' '}

    def mock_get_reimb_by_reimb_id(self, reimb_id):
        return Reimbursement(14, 3000, datetime(2022, 7, 24, 11, 42, 42, 210833),
                             datetime(2022, 7, 25, 11, 42, 42, 210833),
                             2, 2, 'Bracelet - make peace with spouse for spending two nights for work purpose',
                             '/receipts/14.jpeg', 4, 5)

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.update_reimb_by_reimb_id', mock_update_reimb_by_reimb_id)
    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb_by_reimb_id', mock_get_reimb_by_reimb_id)
    # Act and  # Assert
    with pytest.raises(Forbidden):
        reimb_service.update_reimbursement_by_reimb_id(
            {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 14, 2
        )


def test_add_reimbursement_valid_params(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_add_reimb(self, req_id, amount, desc, file, type_id):
        return True

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.add_reimb', mock_add_reimb)
    # Act and
    actual = reimb_service.add_reimbursement(
        {'user_id': 4, 'username': 'valiv9', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
         'user_role': 1}, 5000, "Desc", b'', 3)
    # Assert
    assert actual is True

def test_add_reimbursement_invalid_user(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return None

    def mock_add_reimb(self, req_id, amount, desc, file, type_id):
        return True

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.add_reimb', mock_add_reimb)

    # Act and  # Assert
    with pytest.raises(Unauthorized):
        reimb_service.add_reimbursement(
            {'user_id': 4, 'username': 'logo', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 5000, "Desc", b'', 3)

def test_add_reimbursement_invalid_type(mocker):
    #  Arrange
    def mock_get_user_by_username(self, username):
        return User(4, 'valiv9', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2', 'Valentin',
                    'Vlad', 'vv@a.ca', 1)

    def mock_add_reimb(self, req_id, amount, desc, file, type_id):
        return True

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)
    mocker.patch('dao.reimb_dao.ReimbDao.add_reimb', mock_add_reimb)

    # Act and  # Assert
    with pytest.raises(InvalidParameter):
        reimb_service.add_reimbursement(
            {'user_id': 4, 'username': 'logo', 'first_name': 'Valentin', 'last_name': 'Vlad', 'email': 'vv@a.ca',
             'user_role': 1}, 5000, "Desc", b'', "abc")
