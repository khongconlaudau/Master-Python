        # Type Conversion
# int(x)
# float(x)
# bool(x)
# str(x)


x = input("x: ")
print(type(x))
y = int(x) + 1
print(y)

    # Casting bool() is tricky
# "" or 0 or None is considered False
# Anything else is True

false = "False"
is_opposite = bool(false)
print(is_opposite)