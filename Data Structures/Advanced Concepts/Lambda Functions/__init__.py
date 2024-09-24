 # ----------------------------------------
#          Sorted tuple list
items = [
    ("Product 1", 10),
    ("Product 2", 19),
    ("Product 3", 12)
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
# print(items)

#    Using lambda
items.sort(key=lambda item: item[1])
print(items)
