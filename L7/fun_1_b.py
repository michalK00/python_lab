def median(numbers):
    sorted(numbers)
    return numbers[int(len(numbers)/2)] if len(numbers) % 2 == 1 else (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2)-1]) / 2


if __name__ == "__main__":
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))
