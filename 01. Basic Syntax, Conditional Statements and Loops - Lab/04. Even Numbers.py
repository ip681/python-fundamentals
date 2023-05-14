count_nums = int(input())
is_all_even = True

for i in range (count_nums):
    current_num = int(input())
    if current_num % 2 != 0:
        is_all_even = False
        print(f"{current_num} is odd!")
        break

if is_all_even:
    print("All numbers are even.")
