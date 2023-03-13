import sys


def funC():
    largest_file_size = 0
    largest_file_path = ""
    for line in sys.stdin:
        words = line.split()
        if words[-1] != "-":
            bytes = int(words[-1])
            if largest_file_size < bytes:
                largest_file_size = bytes
                largest_file_path = words[-4]

    print(
        f"File path: {largest_file_path}, {largest_file_size/10 ** 6:.2f} MB")


if __name__ == "__main__":
    funC()
