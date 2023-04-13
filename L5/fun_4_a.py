import random
from fun_2 import to_list_of_dicts


def create_users_set(path):
    users_messages = {}
    for dict in to_list_of_dicts(path):

        if dict["user"] is not None and dict["user"] not in users_messages.keys():
            users_messages[dict['user']] = [dict['message']]
        elif dict["user"] is not None:
            users_messages[dict['user']].append(dict['message'])
    return users_messages


def get_random_user(path):
    return random.choice(list(create_users_set(path).keys()))


def get_n_random_rows_from_random_user(N, path):
    user_rows = create_users_set(path)[get_random_user(path)]
    return random.choices(user_rows, k=min(N, len(user_rows)))
