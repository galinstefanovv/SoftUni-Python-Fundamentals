n = int(input())
positive = list()
negative = list()
positive_counter = 0
negative_sum = 0
for i in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
        positive_counter += 1
    else:
        negative.append(numbers)
        negative_sum += numbers
print(positive)
print(negative)
print(f'Count of positives: {positive_counter}')
print(f'Sum of negatives: {negative_sum}')