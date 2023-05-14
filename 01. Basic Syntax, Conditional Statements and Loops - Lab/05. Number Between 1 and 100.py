number = float(input())

while number < 1 or number > 100:
    number = float(input())

else:
    print(f'The number {number} is between 1 and 100')