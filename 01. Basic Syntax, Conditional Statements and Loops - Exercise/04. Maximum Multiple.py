divisor = int(input())
boundary = int(input())
current_number = boundary

for curr_num in range(boundary, divisor, - 1):
    if 0 < current_number <= boundary and current_number % divisor == 0:
        print(current_number)
        break
    current_number -= 1
