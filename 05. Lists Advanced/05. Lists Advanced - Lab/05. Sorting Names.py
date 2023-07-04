names = input().split(", ")
sorted_names = sorted(names, key=lambda name: (-len(name), name))
print(sorted_names)
