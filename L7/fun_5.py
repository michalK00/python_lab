from fun_2_a import eval_is_fun_unary
from functools import cache
import fun_4_a_b


def make_generator(f):
    @cache
    def memoize_f(f):
        return f

    def custom_generator():
        i = 1
        while True:
            yield memoize_f(f(i))
            i += 1

    return custom_generator


def iterate_n_times(n, f):
    for i, gen in enumerate(make_generator(f)()):
        if i > n:
            break
        # print(f"{i}: {gen}")


if __name__ == "__main__":
    stop_condition = 6000

    # 4_a
    # fibonacci
    print("Fibonacci sequence:")
    iterate_n_times(stop_condition, fun_4_a_b.fibonacci_number)
    print("1st done")
    iterate_n_times(stop_condition, fun_4_a_b.fibonacci_number)
    print("2nd done")
