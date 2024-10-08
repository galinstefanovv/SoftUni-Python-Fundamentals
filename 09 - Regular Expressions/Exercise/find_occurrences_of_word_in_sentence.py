import re

text = input().lower()
word = input().lower()

match = re.findall(rf"\b{word}\b", text)

print(len(match))