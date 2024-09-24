items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

#  if an item has price >=10, it will return an item
fill = list(filter(lambda item: item[1] >=10, items))
print(fill)