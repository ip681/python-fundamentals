text = input()
vowels = ["a", "o", "e", "i", "u"]
no_vowels = [letter for letter in text if letter.lower() not in vowels]
print("".join(no_vowels))
