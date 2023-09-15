import sys

from users import authorization, add_new_user
from calculator import run_app
from file_handler import get_user_history, add_clear_user_data


def main():
    while True:
        print('_ Log in _______________________________________ press 1')
        print('_ Registration _________________________________ press 2')
        print('_ Start calculator _____________________________ press 3')
        print('_ Exit _________________________________________ press 0')
        cmd = input('Choice action: ')

        if cmd.strip() == '1':
            user_menu()

        elif cmd.strip() == '2':
            #  Registration of a new user and launch of the massager
            current_user = add_new_user()
            username = current_user[0]
            run_app(username, current_user=True)

        elif cmd.strip() == '3':
            print('----- Start calculator -----')
            print('There are no operations with trigonometric functions\n'
                  'and the ability to view or save history.')
            run_app()

        elif cmd.strip() == '0':
            print('Have a nice day!')
            sys.exit()
        else:
            print('Wrong input! Repeat choice.')


def user_menu():
    current_user = authorization()
    while True:

        print('_ Start calculator _______________ press 1')
        print('_ Views history __________________ press 2')
        print('_ Clear history __________________ press 3')
        print('_ Exit ___________________________ press 0')
        user_cmd = input('Enter choice: ')
        if user_cmd.strip() == '1':
            print('----- Start app -----')
            run_app(current_user[1], current_user[0])
        elif user_cmd.strip() == '2':
            print('----- Start views history -----')
            get_user_history(current_user[1])

        elif user_cmd.strip() == '3':
            print('----- Start cleaning history -----')
            answ_clear = input('Clear all history? (y/n) ')
            if answ_clear == 'y':
                add_clear_user_data(current_user[1])
                print('----- History is clean -----')

            elif answ_clear == 'n':
                print('Cleaning aborted.')
            else:
                print('Wrong input!')

        elif user_cmd.strip() == '0':
            break
        else:
            print('Wrong input!')


if __name__ == '__main__':
    main()
