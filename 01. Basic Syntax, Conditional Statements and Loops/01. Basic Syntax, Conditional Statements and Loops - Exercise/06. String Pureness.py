lines = int(input())

for strings in range(lines):
    string = str(input())
    if ',' in string or '.' in string or '_' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
