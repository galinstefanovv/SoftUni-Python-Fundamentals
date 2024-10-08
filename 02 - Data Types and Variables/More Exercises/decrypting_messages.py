key = int(input())
lines = int(input())
text = ""
for i in range(1, lines + 1):
    letter = input()
    word = ord(letter) + key
    text += chr(word)
print(text)