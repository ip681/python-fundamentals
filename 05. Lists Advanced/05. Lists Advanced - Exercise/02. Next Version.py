current_version = input().split(".")
version = current_version[0] + current_version[1] + current_version[2]
new_version = int(version) + 1
new_version_lst = [digit for digit in str(new_version)]
print(".".join(new_version_lst))
