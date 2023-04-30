from functools import cache

import fun_4_a_b
import time


# caching the cashed result of a function
@cache
def make_memoized_generator(f):
    func = cache(f)

    # "wrapping" with a lambda, so it is seen as a unary function :D
    return fun_4_a_b.make_generator(lambda x: func(x))


# the same function as fun_4_a_b.iterate_n_times,
# but doesn't print results
def iterate_n_times(n, f):
    for i, gen in enumerate(make_memoized_generator(f)()):
        if i > n:
            break


if __name__ == "__main__":
    stop_condition = 6000

    # 4_a
    # fibonacci
    print("Fibonacci sequence:")

    print(f"1st start: {time.strftime('%X')}")
    iterate_n_times(stop_condition, fun_4_a_b.fibonacci_number)
    print(f"1st end: {time.strftime('%X')}")

    print(f"2nd start: {time.strftime('%X')}")
    iterate_n_times(stop_condition + 1, fun_4_a_b.fibonacci_number)
    print(f"2nd end: {time.strftime('%X')}\n")
