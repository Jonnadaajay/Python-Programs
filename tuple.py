myTuple = ("A","B","C")
tuple = (1,3,"Abc")
for x in tuple:
    print(x)
    
    
tuple1 = (1)
tuple2 = (2,"hi",3.25)
tuple3 = (1,3,3.25)
print(type(tuple1))
print(type(tuple2))
print(len(tuple2))
print(tuple2[1])
print(tuple2[-1])
print(tuple2[0:2])

if "hii" in tuple2:
    print("yes")
else:
    print("no")
    
exlist = list(tuple3)
exlist[1] = "hello"
exlist.append("100")
exlist.remove(3.25)
tuple3 = tuple(exlist)
print(tuple3)

del tuple3
print(tuple3)