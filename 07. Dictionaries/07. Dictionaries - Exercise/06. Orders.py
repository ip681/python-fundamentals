command = input()

drinks_info = {}
price_d = "price"
quantity_d = "quantity"

while command != "buy":
    name, price, quantity = [float(x) if x[-1].isdigit() else x for x in command.split()]
    drinks_info[name] = drinks_info.get(name, {})
    drinks_info[name][price_d] = drinks_info[name].get(price_d, 0)
    drinks_info[name][quantity_d] = drinks_info[name].get(quantity_d, 0)
    drinks_info[name][price_d] = price
    drinks_info[name][quantity_d] += quantity
    command = input()

for product_name in drinks_info:
    result = drinks_info[product_name][price_d] * drinks_info[product_name][quantity_d]
    print(f"{product_name} -> {result:.2f}")




