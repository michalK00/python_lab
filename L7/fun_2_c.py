def atleast(n, pred, iterable):
    # return sum(1 for elem in iterable if pred(elem)) >= n
    counter = 0
    for elem in iterable:
        if pred(elem):
            counter += 1
            if counter >= n:
                return True
    return False


if __name__ == "__main__":
    def fun(x):
        return x <= 5


    some_iterable = [1, 2, 3, 4, 5]
    iterable_size = len(some_iterable)
    print(atleast(iterable_size, fun, some_iterable))
    print(atleast(iterable_size + 1, fun, some_iterable))
