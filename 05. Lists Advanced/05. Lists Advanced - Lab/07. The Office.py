employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())
calculated_happiness = list(map(lambda happiness: happiness * improvement_factor, employees_happiness))
average_happiness = sum(calculated_happiness) / len(calculated_happiness)
happy_list = [item for item in calculated_happiness if item >= average_happiness]
happy_count = len(happy_list)
total_count = len(employees_happiness)
score = happy_count / total_count
if score >= 1 / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
