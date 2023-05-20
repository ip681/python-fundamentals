from math import ceil

people = int(input())
capacity = int(input())

courses = ceil(people / capacity)
print(courses)


# people = int(input())
# capacity = int(input())
#
# if people % capacity == 0:
#     print(int(people / capacity))
#
# else:
#     print(int(people / capacity) + 1)
