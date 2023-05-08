from typing import List, Any


def flatten(to_flatten: List[Any]) -> List[Any]:
    def inner_flattener(to_flatten_inner: List[Any], acc: List[Any]) -> List[Any]:
        match to_flatten_inner:
            case [list(), *tail]:
                return inner_flattener(tail, acc + inner_flattener(to_flatten_inner[0], []))
            case [head, *tail]:
                return inner_flattener(tail, acc + [head])
            case _:
                return acc
    return inner_flattener(to_flatten, []) if len(to_flatten) > 0 else []


if __name__ == "__main__":
    print(flatten([1, [2, 3], [[4, 5], 6]]))
