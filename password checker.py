password = input("Enter your password")
length = len(password) >= 8
upper = any(char.isupper() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in "#@*$?/" for char in password)
if length and upper and digit and special:
    print("strong password")
elif length and (upper or digit or special):
    print("moderate password")
else:
    print("weak password")