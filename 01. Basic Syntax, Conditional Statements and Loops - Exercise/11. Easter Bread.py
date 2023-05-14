budget = float(input())
flour_price = float(input())

easter_bread = 0
colored_eggs = 0
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
easter_bread_price = flour_price + eggs_price + milk_price

while budget > easter_bread_price:
    easter_bread += 1
    budget -= easter_bread_price
    colored_eggs += 3
    if easter_bread % 3 == 0:
        colored_eggs -= easter_bread - 2

print(f'You made {easter_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
