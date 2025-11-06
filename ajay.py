lower = upper = digit = space = special = 0

with open("ajay.txt", 'r') as f:
    text = f.read()

# for ch in text:
#     ch1 = ord(ch)
#     if ch1 >= 97 and ch1 <= 122:
#         lower += 1
#     elif ch1 >= 65 and ch1 <= 90:
#         upper += 1
#     elif ch1 >= 48 and ch1 <= 57:
#         digit += 1
#     elif ch1 == 32:
#         space += 1
#     else:
#         special += 1

# print("Lowercase:", lower)
# print("Uppercase:", upper)
# print("Digits:", digit)
# print("Spaces:", space)
# print("Special characters:",special)
print("now with methods----------------")
for ch in text:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1
print("Lowercase:", lower)
print("Uppercase:", upper)
print("Digits:", digit)
print("Spaces:", space)
print("Special characters:",special)

