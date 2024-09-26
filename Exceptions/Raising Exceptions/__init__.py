def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be less than or equal to zero.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


    # *****   Raising Exception can cause bad performance on a big APPLICATION

