from functools import lru_cache
import fun_4_a_b

# TODO


def make_generator_mem(f):
    @lru_cache(maxsize=None)
    def memoized_f(f):
        return f
    return fun_4_a_b.make_generator(memoized_f(f))


def iterate_n_times_mem(n, f):
    for i, gen in enumerate(make_generator_mem(f)()):
        if i > n:
            break
        # print(f"{i}: {gen}")


if __name__ == "__main__":
    stop_condition = 6000

    # 4_a
    # fibonacci
    print("Fibonacci sequence:")
    iterate_n_times_mem(
        stop_condition, fun_4_a_b.fibonacci_number(stop_condition))
