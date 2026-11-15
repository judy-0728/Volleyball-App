def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


numbers = [1, 2, 3, 4, 5]
total = sum_numbers(numbers)
print(total)
def multiply_numbers(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= numbers
    return result

numbers = [1, 2, 3, 4, 5]
product = multiply_numbers(numbers)
print(product)