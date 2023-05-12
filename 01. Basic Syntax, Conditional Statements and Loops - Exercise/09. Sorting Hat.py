name = input()
voldemort = False

while name != "Welcome!":
    if name == "Voldemort":
        voldemort = True
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if not voldemort:
    print("Welcome to Hogwarts.")
