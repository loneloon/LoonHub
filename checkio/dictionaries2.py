text = '''When I was One
I had just begun
When I was Two
I was nearly new'''

words = ['i', 'was', 'three', 'near']

print(text)
print(words)

word_count = []

for word in words:
    if word in text:
        word_count.append(text.count(word))
    elif word.capitalize() in text:
        word_count.append(text.count(word.capitalize()))
    else:
        word_count.append(0)
print(word_count)

answer = dict(zip(words, word_count))
print(answer)

# Caution! letter sequences get counted anyways! even inside other words!
