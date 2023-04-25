def forall(pred, iterable):
    # cleaner but less readable in my opinion
    # return all(pred(elem) for elem in iterable)
    for elem in iterable:
        if not pred(elem):
            return False
    return True


# I could modify i.e. list class so that I can call [1, 2, 3].forall(lambda x: x>2),
# but I want it to work with all iterables, and the isn't such class to modify
if __name__ == "__main__":
    some_iterable = [1, 2, 3, 4, 5]
    print(forall(lambda x: x <= 5, some_iterable))
    print(forall(lambda x: x < 5, some_iterable))
