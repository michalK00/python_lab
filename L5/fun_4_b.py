from fun_2 import to_list_of_dicts
from type_enum import TypeOfMessage as ms
import datetime


def check_if_session_login_or_logout(log):
    return log["type"] == ms.LOGIN_SUCCESSFUL or log["type"] == ms.CONNECTION_CLOSED


def get_users_sessions(path):
    user_sessions = {}
    filtered_logs = list(filter(
        check_if_session_login_or_logout, to_list_of_dicts(path)))
    sorted_by_sshd = sorted(
        filtered_logs, key=lambda log: log["sshd"])
    for dict in sorted_by_sshd:
        if dict["user"] not in user_sessions.keys():
            user_sessions[dict["user"]] = {}
        if dict["sshd"] not in user_sessions[dict["user"]].keys():
            user_sessions[dict["user"]][dict["sshd"]] = {}
            user_sessions[dict["user"]][dict["sshd"]
                                        ]["login_time"] = None
            user_sessions[dict["user"]][dict["sshd"]
                                        ]["logout_time"] = None

        if dict["type"] == ms.LOGIN_SUCCESSFUL:
            user_sessions[dict["user"]][dict["sshd"]
                                        ]["login_time"] = dict["date"]
        if dict["type"] == ms.CONNECTION_CLOSED:
            user_sessions[dict["user"]][dict["sshd"]
                                        ]["logout_time"] = dict["date"]

    return user_sessions


def calculate_globally(path):
    sessions = get_users_sessions(path)
    session_length = [session["logout_time"] - session["login_time"]
                      for user_sessions in sessions for session in sessions[user_sessions].values() if session["logout_time"] != None and session["login_time"] != None]
    print(session_length)
    # TODO finish calculating average and standard deviation


def calculate_locally(path):
    sessions = get_users_sessions(path)
    users = {}
    for user in sessions:
        if user not in users.keys():
            users[user] = []
        for session in sessions[user].values():
            if session["logout_time"] != None and session["login_time"] != None:
                users[user].append(session["logout_time"] -
                                   session["login_time"])
    print(users)
    # TODO finish calculating average and standard deviation


# don't do tests without this, it runs all the programs that just have a call without that if
# (debugging that ain't fun)
if __name__ == "__main__":
    calculate_locally('./SSH.log')
