n=int(input("Enter a number:"))
f = 1
for i in range(1,n+1):
    f = f*i
    if i == n:
        print("factorial of",n,"is",f)
    