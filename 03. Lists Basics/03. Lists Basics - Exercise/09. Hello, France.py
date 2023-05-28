items_collection = input()
budget = int(input())
ticket_price = 150
items_collection_list = items_collection.split("|")
new_prices_list = []
profit = 0
sold_items_value = 0
budget_is_enough = False
for i in range(len(items_collection_list)):
    current_items = items_collection_list[i]
    current_items_list = current_items.split("->")
    current_item_type = current_items_list[0]
    current_item_price = float(current_items_list[-1])
    if current_item_type == "Clothes" and current_item_price <= 50:
        item_price_is_in_range = True
    elif current_item_type == "Shoes" and current_item_price <= 35:
        item_price_is_in_range = True
    elif current_item_type == "Accessories" and current_item_price <= 20.50:
        item_price_is_in_range = True
    else:
        item_price_is_in_range = False
    if item_price_is_in_range and budget >= current_item_price:
        budget -= current_item_price
        current_item_new_price = current_item_price * 1.4
        profit += current_item_new_price - current_item_price
        sold_items_value += current_item_new_price
        new_prices_list.append(current_item_new_price)
for j in range(len(new_prices_list)):
    new_price = new_prices_list[j]
    print(f"{new_price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
if (sold_items_value + budget) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

