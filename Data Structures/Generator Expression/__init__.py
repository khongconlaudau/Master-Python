from sys import getsizeof

# A list comprehension returns a list while a generator expression returns a generator object.
#
# It means that a list comprehension returns a complete list of elements upfront. However, a generator expression returns a list of elements, one at a time, based on request.
#
# A list comprehension is eager while a generator expression is lazy.
#
# In other words, a list comprehension creates all elements right away and loads all of them into the memory.
#
# Conversely, a generator expression creates a single element based on request. It loads only one single element to the memory.


values = (x * 2 for x in range(100000))
print("gen: ", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list: ", getsizeof(values))