from fun_2_a import eval_is_fun_unary


# a high level function that takes a function that
# it itself takes one parameter
def make_generator(f):
    eval_is_fun_unary(f)

    # generator is suboptimal, as it doesn't memoize (e.g. fibonacci_number will have atrocious time complexity)
    def custom_generator():
        i = 1
        while True:
            yield f(i)
            i += 1

    return custom_generator


def fibonacci_number(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = a + temp
    return a


def iterate_n_times(n, f):
    for i, gen in enumerate(make_generator(f)()):
        if i > n:
            break
        print(f"{i}: {gen}")


if __name__ == "__main__":
    stop_condition = 20

    # 4_a
    # fibonacci
    print("Fibonacci sequence:")
    iterate_n_times(stop_condition, fibonacci_number)

    # 4_b
    print("\nArithmetic sequence:")
    # arithmetic sequence
    iterate_n_times(stop_condition, lambda n: n + 3)

    print("\nGeometric sequence:")
    # geometric sequence
    iterate_n_times(stop_condition, lambda n: n * 3)

    print("\nPower sequence:")
    # power sequence
    iterate_n_times(stop_condition, lambda n: 3 ** n)
