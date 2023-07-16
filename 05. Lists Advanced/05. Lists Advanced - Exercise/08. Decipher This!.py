def decipher(text):
    word_list = list(text)
    digits = []
    letters = []
    for digit in word_list:
        try:
            digits.append(int(digit))
        except ValueError:
            letters.append(digit)
    number = int(''.join(map(str, digits)))
    word_list[0] = chr(number)
    result = [word_list[0]] + letters
    result[1], result[-1] = result[-1], result[1]
    return "".join(result)


secret_message = input().split()
for word in secret_message:
    print(decipher(word), end=" ")
