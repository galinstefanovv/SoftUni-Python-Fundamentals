import sys

n = int(input())
max_number = -sys.maxsize
max_weight = 0
max_distance = 0
max_quality = 0
for i in range(1, n + 1):
    weight = int(input())
    distance = int(input())
    quality = int(input())
    value = int((weight / distance) ** quality)
    if value > max_number:
        max_number = value
        max_weight = weight
        max_distance = distance
        max_quality = quality
print(f'{max_weight} : {max_distance} = {max_number} ({max_quality})')