lines = int(input())
tub_capacity = 255 # Liters
total_water = 0 # Liters

for capacity in range(lines):
    water = float(input())

    if water <= tub_capacity:
        tub_capacity -= water
        total_water += water

    else:
        print("Insufficient capacity!")

print(f"{total_water:.0f}")
