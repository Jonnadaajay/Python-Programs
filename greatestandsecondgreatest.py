list = [6,9,22,5,66]
glist=list[0]
second = list[0]
for x in list:
     if(glist<x):
         second = glist
         glist=x
     elif(second < x and second < glist):
      second = x
print(glist)
print(second)


