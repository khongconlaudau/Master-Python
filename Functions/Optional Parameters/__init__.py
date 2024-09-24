    # Optional Parameters have to come after the required parameter

def increment(number, by=1):
    return number + by

print(increment(5))  # +1 by default
print(increment(5, 5))