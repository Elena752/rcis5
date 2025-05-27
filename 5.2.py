def calculate_stats(numbers):
    sum_positives = sum(num for num in numbers if num > 0)

    min_val = min(numbers)
    max_val = max(numbers)
    min_index = numbers.index(min_val)
    max_index = numbers.index(max_val)

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    product = 1
    for num in numbers[start:end]:
        product *= num

    return sum_positives, product

numbers = [4, 0, -5, 2, 7, -1, 4, -2, 6]
result = calculate_stats(numbers)
print(f"Сумма положительных: {result[0]}, Произведение между min и max: {result[1]}")