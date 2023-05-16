first_char = int(input())
last_char = int(input())

for char in range(first_char, last_char + 1):
    print(chr(char), end=' ')
