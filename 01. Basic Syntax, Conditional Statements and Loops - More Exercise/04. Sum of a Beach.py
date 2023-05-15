input_string = input()
input_string_lower = input_string.lower()
count_sand = 0
count_water = 0
count_fish = 0
count_sun = 0
if "sand" in input_string_lower:
    count_sand = input_string_lower.count('sand')
if "water" in input_string_lower:
    count_water = input_string_lower.count('water')
if "fish" in input_string_lower:
    count_fish = input_string_lower.count('fish')
if "sun" in input_string_lower:
    count_sun = input_string_lower.count('sun')
counter = count_sand + count_water + count_fish + count_sun
print(counter)