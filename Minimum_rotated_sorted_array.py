def find_min(numbers):
    length = len(numbers)
    smallest = numbers[0]
    for i in range(length):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest 