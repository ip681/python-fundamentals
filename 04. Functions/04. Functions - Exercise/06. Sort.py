main_list = [int(n) for n in input().split()]
sort_list = list()


def sorted_l(numbers):
    numbers.sort()
    for n in numbers:
        sort_list.append(n)
    return sort_list


print(sorted_l(main_list))
