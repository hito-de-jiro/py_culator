import re
import sys
from file_handler import get_users_data, write_to_json


def add_new_user():
    """Creates a new user and returns his tuple (login and password)"""
    while True:
        # Creation of a list of logins of valid users
        current_users_login = []
        for users_dict in get_users_data():
            for users in users_dict.keys():
                current_users_login.append(users)

        # Entering and verifying that the login matches
        username = input('Enter name: ')
        if not username or re.findall(r'\s+', username):
            print('Input data must be free of blanks and spaces')
        else:
            if username in current_users_login:
                print('Name is used!')
            else:
                # if there are no matches - entering and checking the password
                print('Password requirements:\n'
                      '1. Minimum of 8 characters, including spaces\n'
                      'but cannot consist of only spaces.\n'
                      '2. The password must contain numbers, letters and\n'
                      'special characters.')
                password = create_user_password()
                # creating a new user
                new_user = {
                    'password': str(password),
                    'log': {},
                }
                user_data = {username: new_user}
                # Adding a new user in JSON
                write_to_json(user_data)
                return username, True


def create_user_password():
    #  Creating and checking a strong password
    while True:
        password = input('Password: ')
        if not password or re.findall(r'^\s+$', password):
            print('Password cannot consist of only spaces')
        else:
            if len(password) < 8:
                print('Password must be min 8 characters.')
            else:
                user_password = _check_password(password)
                return user_password


def _check_password(password):
    pass_regex = re.compile(
        r'^(?=.*?\d)(?=.*?[a-zA-Z])(?=.*?[^A-Za-z\s0-9])')
    if not pass_regex.findall(password):
        print('Password must contain numbers, '
              'letters and special characters.')
    else:
        confirm_password = input('Confirm password: ')
        if password != confirm_password:
            print('Passwords do not match. Repeat input.')
        else:
            return confirm_password


def authorization():
    # User authorization
    while True:
        user_login = input('Enter your login '
                           'or press <ENTER> to exit: ')
        if user_login == '':
            sys.exit()
        elif user_login != '':
            user_password = input('Enter your password'
                                  ' or press <ENTER> to exit: ')
            if user_password == '':
                sys.exit()

            elif check_user(user_login, user_password):
                print('Welcome back ' + user_login + '!')
                return True, user_login
            elif not check_user(user_login, user_password):
                print('Invalid login or password. \nSign in again.')


def check_user(user_login, user_password):
    # Checking the correctness of entering the login and password
    for user_data in get_users_data():
        if user_login in user_data:
            login_is_found = True
            for k, v in user_data.items():
                if k == user_login:
                    password = v['password']
                    if user_password == password:
                        password_is_found = True
                        return login_is_found, password_is_found
