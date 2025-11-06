a=str(input("Enter a string: "))
i = 0
str= " "
while i < len(a):
    str = a[i] + str
    i += 1
print(str)