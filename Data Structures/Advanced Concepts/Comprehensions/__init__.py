#     Instead of using filter and map, we can use comprehension

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]

# Syntax: [(expression) for item in items]

prices = list(map(lambda item: item[1], items))
prices2 = [item[1] for item in items]
print(prices2)

filtered = list(filter(lambda item: item[1] >=10, items))
print(filtered)
filtered2 = [item[1] for item in items if item[1] >= 10]
print(filtered2)


