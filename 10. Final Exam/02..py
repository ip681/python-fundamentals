import re

def sol():
    count = int(input())
    pattern = r'(.+)\>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1'
    for i in range(count):
        password = input()
        result = re.match(pattern, password)
        if result:
            print(f"Password: {result.group(2)}{result.group(3)}{result.group(4)}{result.group(5)}")
        else:
            print("Try another password!")

sol()