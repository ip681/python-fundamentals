def is_valid_length(password):
    return 8 <= len(password)

def consists_only_letters_digits(password):
    return all(char.isalnum() or char == '_' for char in password)

def has_uppercase_letter(password):
    return any(char.isupper() for char in password)

def has_lowercase_letter(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def is_valid_password(password):
    validation_messages = []
    if not is_valid_length(password):
        validation_messages.append("Password must be at least 8 characters long!")
    if not consists_only_letters_digits(password):
        validation_messages.append("Password must consist only of letters, digits, and _!")
    if not has_uppercase_letter(password):
        validation_messages.append("Password must consist at least one uppercase letter!")
    if not has_lowercase_letter(password):
        validation_messages.append("Password must consist at least one lowercase letter!")
    if not has_digit(password):
        validation_messages.append("Password must consist at least one digit!")

    return validation_messages

def manipulate_password(password, commands):
    for command in commands:
        tokens = command.split()
        action = tokens[0]
        if action == "Make":
            _, case, index = tokens
            index = int(index)
            if case == "Upper":
                password = password[:index] + password[index].upper() + password[index + 1:]
                print(password)
            elif case == "Lower":
                password = password[:index] + password[index].lower() + password[index + 1:]
                print(password)
        elif action == "Insert":
            _, index, char = tokens
            index = int(index)
            if 0 <= index <= len(password):
                password = password[:index] + char + password[index:]
                print(password)
        elif action == "Replace":
            _, char, value = tokens
            value = int(value)
            if char in password:
                new_char = chr(ord(char) + value)
                password = password.replace(char, new_char)
                print(password)
        elif action == "Validation":
            validation_results = is_valid_password(password)
            if not validation_results:
                encrypted_password = "".join(chr(ord(char) + 3) for char in password)
                # print(f"Password: {encrypted_password}")
            else:
                print("Try another password!")


initial_password = input()
commands = []
while True:
    command = input()
    if command == "Complete":
        break
    commands.append(command)

manipulate_password(initial_password, commands)