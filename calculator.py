import re
import math
import nums_from_string

from datetime import datetime
from file_handler import overwrite_to_json, get_users_data

alert = 'Invalid value!'


def run_app(username=None, current_user=False):
    # Starting the main cycle
    example_foo_regex = re.compile(r'(sin|cos|tg|ctg)\d+')
    example_regex = re.compile(r'\d+\W\d+')
    user_results = []
    while True:
        example = input('Enter an example without spaces '
                        '(like this: 2+4)'
                        '\nor press <enter> to exit.\n ')
        # Input validation for a registered user
        if current_user:
            if example == '':
                save_user_data(user_results, username)
                break
            elif not example_foo_regex.findall(example) and not \
                    example_regex.findall(example):
                print('Wrong input!')
            else:
                user_results.append(calculation(current_user, example))
        else:
            if example == '':
                break
            else:
                run_without_user(current_user, example,
                                 example_foo_regex, example_regex)


def run_without_user(current_user, example,
                     example_foo_regex, example_regex):
    # Input validation for unregistered user
    if example_foo_regex.findall(example):
        print('You are not eligible for this operation.')
    elif not example_regex.findall(example):
        print('Wrong input!!!')
    else:
        calculation(current_user, example)


def calculation(current_user, example):
    while True:

        operations = {
            '+': additional,
            '-': subtract,
            '*': multiplication,
            '/': division,
        }
        if current_user:
            operations.update({
                'sin': sin,
                'cos': cos,
                'tg': tg,
                'ctg': ctg,
            })

        # Formation and resolution of the example
        for key, operation in operations.items():
            if key in example:
                values = operation(example)
                print(values)
                return values

        if example == '':
            break


def add_example_to_user_data(user_results, username):
    #  Formatting the results to save in JSON
    dt = datetime.today().strftime("%H:%M:%S-%Y/%m/%d")
    full_data = {dt: user_results}
    users_data = get_users_data()
    for user_dict in users_data:
        for k in user_dict.keys():
            if k == username:
                user_dict[k]['log'].update(full_data)
                return users_data


def save_user_data(user_results, username):
    user_data = add_example_to_user_data(user_results, username)
    return overwrite_to_json(user_data)


def additional(example):
    """Addition"""
    try:
        a = int(example.partition('+')[0])
        b = int(example.partition('+')[2])
        res = int(a + b)
        full_result = f"{a} + {b} = {res}"
        return full_result
    except ValueError:
        return alert


def subtract(example):
    """Subtraction"""
    try:
        a = int(example.partition('-')[0])
        b = int(example.partition('-')[2])
        res = int(a - b)
        full_result = f"{a} - {b} = {res}"
        return full_result
    except ValueError:
        return alert


def multiplication(example):
    """Multiplication"""
    try:
        a = int(example.partition('*')[0])
        b = int(example.partition('*')[2])
        res = int(a * b)
        full_result = f"{a} * {b} = {res}"
        return full_result
    except ValueError:
        return alert


def division(example):
    """Division and elimination of division by zero"""
    try:
        a = int(example.partition('/')[0])
        b = int(example.partition('/')[2])
        try:
            res = float(a / b)
            full_result = f"{a} / {b} = {res}"
            return full_result
        except ZeroDivisionError:
            zero_division = 'Cannot be divided by zero.'
            return zero_division
    except ValueError:
        return alert


def sin(example):
    """Sine function"""
    x = nums_from_string.get_nums(example)
    try:
        res = math.sin(float(x[0]))
        full_result = f"sin({x[0]}) = {res}"
        return full_result
    except IndexError:
        return alert


def cos(example):
    """Cosine function"""
    x = nums_from_string.get_nums(example)
    try:
        res = math.cos(float(x[0]))
        full_result = f"cos({x[0]}) = {res}"
        return full_result
    except IndexError:
        return alert


def tg(example):
    """Tangent function"""
    x = nums_from_string.get_nums(example)
    try:
        res = math.tan(float(x[0]))
        full_result = f"tg({x[0]}) = {res}"
        return full_result
    except IndexError:
        return alert


def ctg(example):
    """Cotangent function"""
    x = nums_from_string.get_nums(example)
    try:
        res = 1 / math.tan(float(x[0]))
        full_result = f"ctg({x[0]}) = {res}"
        return full_result
    except IndexError:
        return alert
