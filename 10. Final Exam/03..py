zoo = {"Area": {}}
data_inp = input()

while data_inp != "EndDay":

    command_, data = data_inp.split(": ")

    if command_ == "Add":
        animal_name, needed_food_quantity, area = data.split("-")
        zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
        if area not in zoo["Area"]:
            zoo["Area"][area] = []
        if animal_name not in zoo["Area"][area]:
            zoo["Area"][area].append(animal_name)

    elif command_ == "Feed":
        animal_name, needed_food_quantity = data.split("-")
        if animal_name in zoo:
            zoo[animal_name] -= int(needed_food_quantity)
            if zoo[animal_name] <= 0:
                del zoo[animal_name]
                for pet_names in zoo["Area"].values():
                    if animal_name in pet_names:
                        pet_names.remove(animal_name)
                        break
                print(f"{animal_name} was successfully fed")

    data_inp = input()

if zoo:
    print("Animals:")
    [print(f" {name} -> {quantity}g") for name, quantity in zoo.items() if name != "Area"]

if zoo["Area"]:
    print("Areas with hungry animals:")
    [print(f" {area_name}: {len(zoo['Area'][area_name])}") for area_name in zoo["Area"] if zoo["Area"][area_name]]




# def feeding_animals():
#     class Animal:
#         def __init__(self, name, food, area):
#             self.name = name
#             self.food = food
#             self.area = area
#
#     def handle_add(map_animals, name, food_quantity, area, hungry_animals):
#         if name not in map_animals:
#             animal = Animal(name, food_quantity, area)
#             map_animals[name] = animal
#         else:
#             old_food_quantity = map_animals[name].food
#             map_animals[name].food = food_quantity + old_food_quantity
#
#         if area not in hungry_animals:
#             hungry_animals[area] = 1
#         else:
#             count_value = hungry_animals[area]
#             hungry_animals[area] = count_value + 1
#
#     def handle_feed(map_animals, name, food_quantity, hungry_animals):
#         if name in map_animals:
#             animal = map_animals[name]
#             food_needed = animal.food
#             feed_result = food_needed - food_quantity
#             if feed_result > 0:
#                 animal.food = feed_result
#             else:
#                 print(f"{name} was successfully fed")
#                 living_area = animal.area
#                 value = hungry_animals[living_area]
#                 hungry_animals[living_area] = value - 1
#                 if hungry_animals[living_area] == 0:
#                     del hungry_animals[living_area]
#                 del map_animals[name]
#
#     map_animals = {}
#     hungry_animals = {}
#
#     while True:
#         command = input()
#         if command == "EndDay":
#             break
#
#         action, data = command.split(": ")
#         animal_name, *params = data.split("-")
#
#         if action == "Add":
#             handle_add(map_animals, animal_name, int(params[0]), params[1], hungry_animals)
#         elif action == "Feed":
#             handle_feed(map_animals, animal_name, int(params[0]), hungry_animals)
#
#     print("Animals:")
#     for animal_name, animal in sorted(map_animals.items(), key=lambda x: x[0]):
#         print(f" {animal_name} -> {animal.food}g")
#
#     print("Areas with hungry animals:")
#     for area, count in sorted(hungry_animals.items(), key=lambda x: -x[1]):
#         print(f" {area}: {count}")
#
#
# feeding_animals()