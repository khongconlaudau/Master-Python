def say_hello():
    print("Hello World")
    print("Welcome to Python")


say_hello()

    # All functions return None by default
def say_hi_to(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

say_hi_to(last_name="Van", first_name="Mason")

def get_say_hi_to(first_name):
    return f"Hello {first_name}"

print(get_say_hi_to(first_name="Mason"))