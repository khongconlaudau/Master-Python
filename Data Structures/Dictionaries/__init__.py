point = {"x": 1, "y": 2,}
 # Here is 2 ways to define dictionaries
point = dict(x=1, y=2, z=3)
point["g"] = 20
for x in point.items():   # .items() converts each key and value to tuple
    print(x)
if "a" in point:
    print(point["a"])

print(point.get("a", 0))   #uses Get to avoid exception, if "a" does not exist return 0
del point["x"]

for key, value in point.items():
    print(key, value)
