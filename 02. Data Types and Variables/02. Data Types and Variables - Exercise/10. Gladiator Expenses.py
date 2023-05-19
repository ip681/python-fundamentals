lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield_count = 0

for fight in range(1, lost_fight+1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        expenses += shield_price
        broken_shield_count += 1
    if broken_shield_count == 2:
        broken_shield_count = 0
        expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')