from fun_2_a import eval_is_fun_unary


def exists(pred, iterable):
    eval_is_fun_unary(pred)
    # return any(pred(elem) for elem in iterable)
    for elem in iterable:
        if pred(elem):
            return True
    return False


if __name__ == "__main__":
    some_iterable = [1, 2, 3, 4, 5]
    print(exists(lambda x: x > 5, some_iterable))
    print(exists(lambda x: x == 2, some_iterable))
