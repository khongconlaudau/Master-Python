from itertools import count

is_successful = False
for numbers in range(1, 4):
    print(f"Attempt {numbers}")
    if is_successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and Failed")
count = 0
for numbers in range(2, 10):
    if numbers % 2 == 0:
        count += 1
        print(numbers)
else:
    print(f"We have {count} even numbers")