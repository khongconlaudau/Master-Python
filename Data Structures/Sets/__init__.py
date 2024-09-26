
# Set is defined by curly braces
# Set does not use index to get element
# Set takes only unique
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# first.add(2)
# first.remove(4)
# print(len(first))
# print(first)
# print(first | second)  # likes pipe in linux.Combines 2 set to a new one
print(first & second)  # find the common attribute in the sets
# print(first - second)  # find the different attributes of the first set from the second
# print(first ^ second)  # find the different in both the 2 sets
