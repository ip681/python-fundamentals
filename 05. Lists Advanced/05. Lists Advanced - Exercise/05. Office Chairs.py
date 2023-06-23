number_of_rooms = int(input())
free_chairs = []
chairs_are_enough = True
for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    current_chairs = len(chairs_and_visitors[0])
    current_visitors = int(chairs_and_visitors[1])
    if current_chairs >= current_visitors:
        free_chairs.append(current_chairs - current_visitors)
    else:
        chairs_are_enough = False
        needed_chairs = current_visitors - current_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
if chairs_are_enough:
    print(f"Game On, {sum(free_chairs)} free chairs left")
