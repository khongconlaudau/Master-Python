# when the tuple is defined, we cannot append or modify the tuple

point = (1, 2) + (3, ) + (5, 6)
print(type(point))
print(point)

# convert list to tuple
tuple1 = tuple([1, 2, 3])
x, y, z = tuple1
print(tuple)

tuple2 = tuple("Hello World")
print(tuple2)
print(tuple2[::-1])

# *****  using tuple to swap variable
# Instead of:
x = 10
y = 11

temp = x
x = y
y = temp

# We can do like this
x, y = y, x  #tuple
