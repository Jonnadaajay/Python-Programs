import re

password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?& ]{8,}$')
print(type(password_pattern))

password = ["Hello@123", "weakpass", "StrongPass@2025"]
for pw in password:
    if password_pattern.match(pw):
        print("Valid password", pw)
    else:
        print("Invalid password", pw)