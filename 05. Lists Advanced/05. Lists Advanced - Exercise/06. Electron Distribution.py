starting_electrons = int(input())
number_of_electrons = starting_electrons
position = 0
electrons_list = []
while number_of_electrons > 0:
    position += 1
    current_electrons = 2 * (position ** 2)
    if sum(electrons_list) + current_electrons <= starting_electrons:
        electrons_list.append(current_electrons)
        number_of_electrons -= current_electrons
    else:
        electrons_list.append(number_of_electrons)
        break
print(electrons_list)
