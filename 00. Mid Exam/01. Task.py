def calculate_provision(days, players, energy, water_per_person, food_per_person, energy_loss):
    total_water = days * players * water_per_person
    total_food = days * players * food_per_person

    for day in range(1, days + 1):
        energy -= energy_loss[day - 1]

        if energy <= 0:
            return f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water."

        if day % 2==0:
            water_to_drink = 0.3 * total_water
            energy += 0.05 * energy
            total_water -= water_to_drink

        if day % 3 == 0:
            food_to_eat = total_food / players
            energy *= 1.1
            total_food -= food_to_eat

    return f"You are ready for the quest. You will be left with - {energy:.2f} energy!"


days = int(input())
players = int(input())
energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

energy_loss = []
for _ in range(days):
    energy_loss.append(float(input()))

result = calculate_provision(days, players, energy, water_per_person, food_per_person, energy_loss)
print(result)