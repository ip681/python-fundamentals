import string

usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char not in "-_" + string.ascii_letters + string.digits:
                break

        else:
            print(username)

