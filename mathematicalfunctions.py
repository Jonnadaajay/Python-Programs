mySet = {"A", "B", 10}
mySet2 = {10, 20,30}
# set3 = mySet.difference(mySet2)\\gives elements in mySet not in mySet2
set3 = mySet - mySet2
print(set3)

# mySet3 = mySet.union(mySet2)\\combines both sets
# mySet3 = mySet.intersection(mySet2)#gives common elements
# mySet3 = mySet | mySet2
# mySet4 = mySet.union(mySet2)
# mySet.update(mySet2)
# print(mySet3)

# mySet.intersection_update(mySet2)
# print(mySet)