# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4] + [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def double_list(numbers) -> list:
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

numbers = [1, 2, 3, 4]
print(double_list(numbers)) # [2, 4, 6, 8]