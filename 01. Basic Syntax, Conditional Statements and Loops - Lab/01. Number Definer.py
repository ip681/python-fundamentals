number = float(input())
number_type = None
number_size = ""

if number == 0:
    number_type = "zero"
elif number > 0:
    number_type = "positive"
elif number < 0:
    number_type = "negative"

if 0 < abs(number) < 1:
    number_size = "small "
elif abs(number) > 1_000_000:
    number_size = "large "

print(f"{number_size}{number_type}")