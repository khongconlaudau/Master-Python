# We can use unpacking operator to take out individual values in any iterable

list = [1, 2, 3]
print(list)
print(*list)
print(1, 2, 3)

values = [*range(5), *"Hello"]
print(values)

first = [1, 2, 3]
second = [4, 5, 6]
print(*first, "a", *second, *"Hello")

first_dict = {"x": 1, "y": 2, "z": 3}
second_dict = {"x": 10, "g": 5, "h": 6}
combined = {**first_dict, **second_dict, "q": 26 }
print(combined)