from string import ascii_letters

text = "Я не стану программистом на Python"

i = 0
text = list(text)
print(text)
while i < len(text):
    if text[i] in ascii_letters:
        text[i] = text[i].upper()
    i += 1

text = "".join(text)
print(text)