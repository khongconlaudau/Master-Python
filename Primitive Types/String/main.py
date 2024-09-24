course = "Python Programming"
say_something = """ 
Hello World
How r yall doing
"""
print(course)
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print(say_something)


         # ESCAPE SEQUENCE
# 1. \"
# 2. \'
# 3. \\
# 4. \n

quote  = "One life no \"Regret\""
print(quote)

        # FORMATTED STRING
first = "Mason"
last = "Van"

full = f"{first} {last}"
        # OR
print(f"{first} {last}")

# Includes space
length = f"{len(full)}"
print(length)