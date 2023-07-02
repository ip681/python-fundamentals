numbers_string = input().split(", ")
numbers = list(map(int, numbers_string))
indices = []
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        indices.append(index)
print(indices)
