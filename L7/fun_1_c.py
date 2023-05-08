def sqrt(x, epsilon=0.01):
    y = x / 2

    def sqrt_helper(y, epsilon):
        return sqrt_helper((y + x / y) / 2, epsilon) if abs(y ** 2 - x) > epsilon else y

    return sqrt_helper(x, epsilon)


if __name__ == "__main__":
    print(sqrt(3, epsilon=0.1))
