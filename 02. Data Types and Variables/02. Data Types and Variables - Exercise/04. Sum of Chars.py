lines = int(input())
sum_chars = 0

for characters in range(lines):
    char = ord(input())
    sum_chars += char

print(f"The sum equals: {sum_chars}")
