# Search with a sequence that starts with 'he"
# followed by two (any) Characters, And an "o"
import re
# txt = "the hello rn in 12 helo 45 spn"
# x = re.findall("he..o", txt)
# print(x)


# check if string starts with 'helllo':
# x = re.findall("he.", txt)
# print(x)
# if x:
#     print("Yes, the string starts with mca", x)
# else:
#     print("No match")
    
# txt = "h rn in 12 helo 45 spn"
# x = re.findall("he.*o", txt)
# print(x)

txt = "hello rn in 12 45 spn"
x = re.findall("he.?o", txt)
print(x)

