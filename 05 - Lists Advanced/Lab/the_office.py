emp = input().split(" ")
factor = int(input())
emp = list(map(lambda x: int(x) * factor, emp))
filtered = list(filter(lambda x: x >= (sum(emp) / len(emp)), emp))
if len(filtered) >= len(emp) / 2:
    print(f'Score: {len(filtered)}/{len(emp)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(emp)}. Employees are not happy!')