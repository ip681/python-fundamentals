population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
countries_count = len(population)
if sum(population) < countries_count * minimum_wealth:
    print("No equal distribution possible")
else:
    while min(population) < minimum_wealth:
        for index, country in enumerate(population):
            if country < minimum_wealth:
                difference = minimum_wealth - country
                population[index] += difference
                max_population_index = population.index(max(population))
                population[max_population_index] -= difference
    print(population)