from array import array

# Array is used when you are dealing with a large sequence of number and encounter performance problems

numbers = array("i",[1, 2, 3, 4, 5])
numbers.append(6)
print(numbers)