mylist = [3,5,7,50,2,1]
first = -1
secnod = -1
for num in mylist:
    if num>first:
        second = first
        first = num
    elif num < first & num > secnod:
        second = num
print(secnod)