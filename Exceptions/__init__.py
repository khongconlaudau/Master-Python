try:
    # Cleaning Up
    file = open("app.py")
    age = int(input("Enter your age: "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
    # OR
# except ZeroDivisionError:
#     print("Age cannot be zero")
else:
    print("Everything is running perfect")
finally:
    # this is cleaning up
    file.close()


print("Done")