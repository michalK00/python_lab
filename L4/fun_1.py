from os import environ
import sys


def env_variables(args):
    # Do refactoringu
    if args:
        envs = [env for env in environ if env in args]
    else:
        envs = list(environ.keys())
    for env in envs:
        print(f"{env} = {environ[env]}")


if __name__ == "__main__":
    env_variables(sys.argv[1:])
