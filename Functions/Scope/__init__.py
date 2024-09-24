message = "a"

def greet(name):
    # global message           # Bad practice. Should avoid all the time
    message = "b"

greet("Mason")
print(message)