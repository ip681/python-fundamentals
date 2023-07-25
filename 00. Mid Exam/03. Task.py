def calc_damage(numbers, target_index, size):
    left_sum = sum(num for num in numbers[:target_index] if is_valid(num, numbers[target_index], size))
    right_sum = sum(num for num in numbers[target_index + 1:] if is_valid(num, numbers[target_index], size))

    if left_sum>=right_sum:
        return f"Left - {left_sum}"
    else:
        return f"Right - {right_sum}"


def is_valid(number, target_number, size):
    if size == "cheap":
        if target_number > number:
            return True
    else:
        if target_number <= number:
            return True
    return False


numbers = list(map(int, input().split(',')))
target_index = int(input())
size = input()

result = calc_damage(numbers, target_index, size)
print(result)


# def calc_damage(items, e_point, i_type):
#     left_damage = sum(items[:e_point])
#     right_damage = sum(items[e_point + 1:])
#
#     if i_type == "cheap":
#         if left_damage <= right_damage:
#             return f"Left - {left_damage}"
#         else:
#             return f"Right - {right_damage}"
#     elif i_type == "expensive":
#         if left_damage >= right_damage:
#             return f"Left - {left_damage}"
#         else:
#             return f"Right - {right_damage}"
#
#
# price_ratings = [int(x) for x in input().split(", ")]
# entry_point = int(input())
# item_type = input()
#
# result = calc_damage(price_ratings, entry_point, item_type)
# print(result)
