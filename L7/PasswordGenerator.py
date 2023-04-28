import string
import random


class PasswordGenerator:
    def __init__(self, length, count, charset=string.ascii_letters + string.digits):
        self.length = length
        self.charset = charset
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        result = self.generate_pass()
        self.index += 1
        return result

    def generate_pass(self):
        return ''.join(random.choices(self.charset, k=self.length))


if __name__ == "__main__":
    generator1 = PasswordGenerator(4, 3)
    generator2 = PasswordGenerator(2, 3)

    passwords1_1 = [password for password in generator1]
    passwords1_2 = [password for password in generator1]
    print(passwords1_1)
    print(passwords1_2)
    print(
        f"Z funkcją next() 1.{next(generator2)} 2.{next(generator2)} 3.{next(generator2)}")
    next(generator2)
