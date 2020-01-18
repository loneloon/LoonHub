text = "Hello world!"

letters = {}

for l in text:
    letters[l] = text.count(l)

print(letters)
print(max(letters.values()))

max_letter = 0

for letter, count in letters.items():
    if count == max(letters.values()):
        max_letter = letter
        break

print(max_letter)

#This prints out the most frequently used letter in a given text
