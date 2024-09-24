# Find the most common character in the String
setence = "This is a common interview question"

repeat = setence.count(setence[0])
char = setence[0]

for character in setence:
    if repeat < setence.count(character):
        char = character
        repeat = setence.count(character)

print(char, repeat)


#  SOLUTION 2

char_frequency = {}
for char in setence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char_frequency = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
print(sorted_char_frequency[0])