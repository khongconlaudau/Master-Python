def multiply(*numbers): # This is called tuple
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5))