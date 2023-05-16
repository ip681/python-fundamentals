key = int(input())
lines = int(input())
string = ''

for word in range(lines):
    letter = ord(str(input())) + key
    string += chr(letter)

print(string)
