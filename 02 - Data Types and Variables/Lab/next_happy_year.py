year = int(input())
happy = False

while not happy:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy = len(set_year) == len(str(year))

print(year)