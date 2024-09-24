from itertools import count

letters = ["a", "b", "c", "b"]

# Add
letters.append("d")
letters.insert(0,"-")
print(letters)

# Remove
# letters.pop()
# letters.remove("b")
# del letters[0:3]
# letters.clear()  # remove all the item
print(letters)   # remove the first matching letter from the index 0

print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

letters.reverse()
# letters.sort()   # sort in ascending order
# letters.sort(reverse=True)  # sort in descending order
print(sorted(letters))  # sorted a copy of the list
print(letters)



