number = int(input())
divider = 0
for num in range(number):
    divider += 1
    if 1 < divider < number and number % divider == 0:
        print('False')
        break
else:
    print('True')
