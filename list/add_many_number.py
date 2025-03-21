# Write a function that takes a list of numbers and returns the sum of those numbers. 

def add_many_number(numbers) -> int:

    total = 0
    for number in numbers:
        total += number 
    return total

print(add_many_number([1, 2, 3, 4, 5])) # 15
print(add_many_number([1, 2, 3, 4, 5, 6])) # 21
    