numbers_sequence = list(map(int, input().split()))
removed_pokemons = []
while len(numbers_sequence) > 0:
    current_index = int(input())
    if current_index < 0:
        removed = numbers_sequence[0]
        numbers_sequence[0] = numbers_sequence[-1]
    elif current_index >= len(numbers_sequence):
        removed = numbers_sequence[-1]
        numbers_sequence[-1] = numbers_sequence[0]
    else:
        removed = numbers_sequence.pop(current_index)
    removed_pokemons.append(removed)
    result_list = []
    for number in numbers_sequence:
        if number <= removed:
            result_list.append(number + removed)
        else:
            result_list.append(number - removed)
    numbers_sequence = result_list.copy()
print(sum(removed_pokemons))
