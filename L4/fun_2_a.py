import os


def parse_path():
    return list(filter(lambda elem: len(elem) > 0, os.environ["PATH"].split(os.pathsep)))


if __name__ == "__main__":
    for path in parse_path():
        print(path)
