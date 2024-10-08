my_list = [int(n) for n in input().split(', ')]
positive = [pos for pos in my_list if pos >= 0]
negative = [neg for neg in my_list if neg < 0]
even = [ev for ev in my_list if ev % 2 == 0]
odd = [od for od in my_list if od % 2 != 0]

print(f"Positive: {', '.join(str(n) for n in positive)}")
print(f"Negative: {', '.join(str(n) for n in negative)}")
print(f"Even: {', '.join(str(n) for n in even)}")
print(f"Odd: {', '.join(str(n) for n in odd)}")