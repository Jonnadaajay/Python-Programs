# mytuple1 = (1, 2, 3)
# (A, B, C) = mytuple1
# print(A, B, C)
# for x in mytuple1:
#     print(x)
    
# n = len(mytuple1)
# i = 0
# while i < n:
#     print(mytuple1[i])
#     i += 1
    
# tupleA =("a","b","c")
# tupleB = (1,3,5)
# print(tupleA + tupleB)

# newTuple = tupleA * 3
# print(newTuple)

# print(tupleA.count("a"))
# print(tupleA.index("a"))

mySet = {"A", "B", 1, 0, "A", "C", True, False}
mySet2 = {10, 20, 30}

# for x in mySet:
#     print(x)
    
while True:
    if len(mySet) == 0:
        break
    mySet.pop()
    print(mySet)
# mySet2.clear()\\clear the set values o\p is set()
# del mySet2
# mySet2.pop()
# mySet.discard("A")#doesnot give error if word doesnot present
# mySet.remove("A")//give error if word doesnot present
# mySet.update(mySet2)
# mySet.add("abcd")
# print(mySet2)
# print(type(mySet))
# print("A" in mySet)
# print("ABC" not in mySet)

# for x in mySet:
#     print(x)
    
# print(len(mySet))


