items = [
    ("Product 1", 10),
    ("Product 2", 13),
    ("Product 3", 12),
    ("Product 4", 10)
]

#  if an item has price >=10, it will return an item
fill = list(filter(lambda item: item[1] >=10, items))
print(fill)