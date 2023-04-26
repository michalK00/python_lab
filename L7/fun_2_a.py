from inspect import signature, isfunction


def eval_is_fun_unary(some_func):
    if not (isfunction(some_func) and len(signature(some_func).parameters) == 1):
        raise TypeError("Predicate must be a unary function!")


def forall(pred, iterable):
    eval_is_fun_unary(pred)

    # cleaner but less readable (in my opinion)
    # return all(pred(elem) for elem in iterable)
    for elem in iterable:
        if not pred(elem):
            return False
    return True


def a_fun(a, b):
    return a+b


# I could modify e.g. list class so that I can call [1, 2, 3].forall(lambda x: x>2),
# but I want it to work with all iterables and there isn't such class to modify
if __name__ == "__main__":
    some_iterable = [1, 2, 3, 4, 5]
    print(forall(lambda x: x <= 5, some_iterable))
    print(forall(lambda x: x < 5, some_iterable))