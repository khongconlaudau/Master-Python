items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# price = []
#
# for item in items:
#     price.append(item[1])
#
# print(price)

#  -------------- Map Function ----------------
# The map() function in Python applies a given function to each item of an iterable (like a list, tuple, etc.) and returns a map object (which is an iterator)
#  You can later convert this iterator into a list, tuple, or another collection type.
price = list(map(lambda item: item[1], items))  #map(func, *iterables) --> map object

    # Make an iterator that computes the function using arguments from
    # each of the iterables.  Stops when the shortest iterable is exhausted.

print(price)
