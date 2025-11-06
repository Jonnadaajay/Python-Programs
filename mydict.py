mydict = {
    "A":1,
    "B":2,
    "c":True,
    "D":3.8,
    10:"Ajay",
    12:"Vijay",
    "mylist":[1,2,3,4,5]
}
# print(mydict)
# print(mydict["mylist"])
# print(len(mydict))
# y = mydict["B"]
# z = mydict.get("B")
# print(y)
# print(z)

# allkeys = mydict.keys()
# print(allkeys)

# mydict["b"] = 33
# allkey2 = mydict.keys()

# print(allkey2)
# print(mydict["B"])

allvalues = mydict.values()
y = allvalues
print(y)

# mydict.clear()
# print(mydict)

for x,y in mydict.items():
    print(x,y)
    
