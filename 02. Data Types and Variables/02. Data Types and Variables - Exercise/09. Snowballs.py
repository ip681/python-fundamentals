import sys

snowballs_qty = int(input())

max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0
max_snowball_value = -sys.maxsize

for snowball in range(1, snowballs_qty+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
        max_snowball_value = snowball_value

print(f'{max_snowball_snow} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})')
