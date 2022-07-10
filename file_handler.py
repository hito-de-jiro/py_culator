import json

filename = 'users_DB.json'


# Отримує або створює JSON
def get_users_data():
    try:
        return get_json_data()
    except FileNotFoundError:
        return create_json()


#  Створення json
def create_json():
    data = []
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))
    return data


#  Отримання даних з json і конв. в словник
def get_json_data():
    with open(filename) as f:
        users_data = json.load(f)
    return users_data


#  Оновлення даних в JSON
def write_to_json(user_data):
    users_data = get_users_data()
    users_data.append(user_data)
    with open(filename, 'w') as f:
        json.dump(users_data, f, indent=2)


# Перезапис JSON
def overwrite_to_json(user_data):
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=2)


# # Отримання журналу юзверя
# def get_user_history(username):
#     users_data = get_json_data()
#     for user_data in users_data:
#         for k, v in user_data.items():
#             if k == username:
#                 user_dict = v['log']
#                 if user_dict:
#                     print('Your history')
#                     for x, values in user_dict.items():
#                         print(x)
#                         for value in values:
#                             print(f'\t{value}')
#                     break
#                 else:
#                     print('You don`t have any history')
#                     return user_dict
# Отримання журналу юзверя
def get_user_history(username):
    users_data = get_json_data()
    for user_data in users_data:
        for k, v in user_data.items():
            if k == username:
                user_dict = v['log']
                print(_get_user_dict(user_dict))
            else:
                print('You don`t have any history')


#  Форматування даних користувача
def _get_user_dict(user_dict):
    for key, values in user_dict.items():
        print(f'{key}: ')
        for value in values:
            print(f'\t{value}')


# Підготовка журнала до очищення
def create_clear_user_history(username):
    users_data = get_users_data()
    for user_dict in users_data:
        for k in user_dict.keys():
            if k == username:
                user_dict[k]['log'] = {}
                return users_data


#  Перезапис очищених файлів
def add_clear_user_data(username):
    clear_data = create_clear_user_history(username)
    return overwrite_to_json(clear_data)
