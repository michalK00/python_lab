# def flatten(elements):
#     def flatten_helper(elements, acc):
#         return flatten_helper(elements[0], acc) + flatten_helper(elements[1:], acc) if isinstance(elements[0], list) or isinstance(elements[0], tuple) else flatten_helper(elements[1:], acc + [elements[0]])
#     return flatten_helper(elements, list())

def flatten(elements):

    def flatten_helper(elements, acc):
        match elements[0]:
            case list():
                return flatten_helper(elements[0], list()) + flatten_helper(elements[1:], acc) if len(elements) > 1 else acc + flatten_helper(elements[0], list())
            case tuple():
                return flatten_helper(elements[0], list()) + flatten_helper(elements[1:], acc) if len(elements) > 1 else acc + flatten_helper(elements[0], list())
            case other:
                return flatten_helper(elements[1:], acc + [elements[0]]) if len(elements) > 1 else acc + [elements[0]]
    return flatten_helper(elements, list()) if len(elements) > 0 else []


if __name__ == "__main__":
    print(flatten([1, [2, 3], [[4, 5], 6]]))
