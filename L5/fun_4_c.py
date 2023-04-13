from fun_2 import to_list_of_dicts
from type_enum import TypeOfMessage as ms
from collections import namedtuple


def get_users_logins(path):
    user_logins = {}
    for dict in to_list_of_dicts(path):
        if dict["user"] is not None and dict["type"] == ms.LOGIN_SUCCESSFUL:
            if dict["user"] not in user_logins.keys():
                user_logins[dict['user']] = 1
            else:
                user_logins[dict['user']] += 1
    return user_logins


def users_who_logged_in_least_and_most_frequently(path):
    user_logins = get_users_logins(path)
    # print(user_logins)
    max_user = max(user_logins, key=user_logins.get)
    min_user = min(user_logins, key=user_logins.get)
    Users = namedtuple("Users", ['least_logged_in', 'most_logged_in'])
    return Users(min_user, max_user)
