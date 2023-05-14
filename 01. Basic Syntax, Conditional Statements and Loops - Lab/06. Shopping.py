budget = int(input())
total_sum = 0
command = input()
money_is_enough = True
while command != "End":
    product_price = int(command)
    total_sum += product_price
    if budget < total_sum:
        print("You went in overdraft!")
        money_is_enough = False
        break
    command = input()
if money_is_enough:
    print("You bought everything needed.")