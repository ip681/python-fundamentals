year = int(input())
happy_year = False

while not happy_year:
    year += 1
    set_year = set()

    for years in range(len(str(year))):
        set_year.add(str(year)[years])

        happy_year = len(set_year) == len(str(year))

print(year)
