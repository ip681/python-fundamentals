first_sequence = input().split(", ")
second_sequence = input().split(", ")
result = []
for index in range(len(first_sequence)):
    for word in second_sequence:
        if first_sequence[index] in word:
            if first_sequence[index] not in result:
                result.append(first_sequence[index])

print(result)
