input_integers = input()
count_to_remove = int(input())
strings_list = input_integers.split(" ")
integers_list = ([int(x) for x in strings_list])
for i in range(count_to_remove):
    integers_list.remove(min(integers_list))
for j in range(len(integers_list)):
    if j == 0:
        print(integers_list[j], end="")
    else:
        print(f", {integers_list[j]}", end="")

