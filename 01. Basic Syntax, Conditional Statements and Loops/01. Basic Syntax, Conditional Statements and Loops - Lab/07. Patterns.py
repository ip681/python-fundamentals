num = int(input())
star = "*"

for i in range(1, 2*num+1):
    print((num - abs(num - i)) * star)