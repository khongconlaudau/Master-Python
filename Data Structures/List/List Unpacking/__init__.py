numbers = [1, 2, 3, 4, 4, 5, 5, 6]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Or using list unpacking: Can use for both list and tuple
#  ***** The variables on the left size must be equal to the number of items that we have on the list

# first, second, third = numbers
# print(first, second, third)

first,second,*others = numbers
print(first, second)
print(others)

first, *others, last = numbers
print(first, others, last)

