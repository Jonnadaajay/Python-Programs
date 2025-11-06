#calucation of arithmetic operation
a=int(input("enter frist number:"))
b=int(input("enter second number:"))
print("addition:")
print("subtraction:")
print("multiplication:")
print("division:")
print("modulus:")
choose=input("choose operation: 1 for addition, 2 for subtraction,3 for multiplication, 4 for division, 5 for modulus:")
if choose == "1":
    print("result:",a + b)
elif choose == "2":
    print("result:",a-b)
elif choose == "3":
    print("result:",a*b)
elif choose == "4":
    print("result:",a/b)
elif choose == "5":
    print("result:",a%b)
else:
    print("invalid operation")