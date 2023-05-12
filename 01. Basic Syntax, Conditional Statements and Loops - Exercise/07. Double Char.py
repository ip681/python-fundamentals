word = input()
while word != "End":
    if word != "SoftUni":
        for char in word:
            print(char * 2, end='')
        print()
    word = input()
