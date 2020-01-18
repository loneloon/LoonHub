import string

text = "bbaaccdd"

alphabet = string.ascii_letters[:28]

text = text.lower()
letters = {}
for l in text:
    letters[l] = text.count(l)

max_letter = []
max_letter_index = {}

for letter, count in letters.items():
    if count == max(letters.values()):
        max_letter.append(letter)

for f in max_letter:
    max_letter_index[f] = alphabet.find(f)

result = 0

for lttr, idx in max_letter_index.items():
    if idx == min(max_letter_index.values()):
        result = lttr
print(result)