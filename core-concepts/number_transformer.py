def transform_numbers(numbers, operations):
    result = []
    
    for number in numbers:
        result.append(number)

    return result

numbers = [2, 4, 6, 8]

squared = transform_numbers(numbers, lambda x: x*x)
multiplaid = transform_numbers(numbers, lambda x: x*10)
added = transform_numbers(numbers, lambda x: x+5)

print(f"Original list: {numbers}")
print(f"squared: {squared}")
print(f"Multiplaid: {multiplaid}")
print(f"added: {added}")

