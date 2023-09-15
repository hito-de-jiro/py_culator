import json

filename = 'users_DB.json'


def get_users_data():
    # Gets or creates JSON
    try:
        return get_json_data()
    except FileNotFoundError:
        return create_json()


def create_json():
    #  Generating json
    data = []
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))
    return data


def get_json_data():
    #  Receiving data from json and conv. in the dictionary
    with open(filename) as f:
        users_data = json.load(f)
    return users_data


def write_to_json(user_data):
    #  Updating data in JSON
    users_data = get_users_data()
    users_data.append(user_data)
    with open(filename, 'w') as f:
        json.dump(users_data, f, indent=2)


def overwrite_to_json(user_data):
    # Rewrite JSON
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=2)


def get_user_history(username):
    # Receiving the user log
    users_data = get_json_data()
    for user_data in users_data:
        for k, v in user_data.items():
            if k == username:
                user_dict = v['log']
                print(_get_user_dict(user_dict))
            else:
                print('You don`t have any history')


def _get_user_dict(user_dict):
    #  Formatting user data
    for key, values in user_dict.items():
        print(f'{key}: ')
        for value in values:
            print(f'\t{value}')


# Preparing the log for cleaning
def create_clear_user_history(username):
    users_data = get_users_data()
    for user_dict in users_data:
        for k in user_dict.keys():
            if k == username:
                user_dict[k]['log'] = {}
                return users_data


#  Overwriting cleaned files
def add_clear_user_data(username):
    clear_data = create_clear_user_history(username)
    return overwrite_to_json(clear_data)
