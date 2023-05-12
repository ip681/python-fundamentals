divisior = int(input())
boundary = int(input())
current_number = boundary

for curr_num in range(boundary, divisior, - 1):
    if 0 < current_num <= boundary and current_number % divisior == 0:
        print(current_number)
        break
    current_number -= 1
