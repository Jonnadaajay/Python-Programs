n=int(input("Enter a number:"))
i = 1
count = 0
while i<=n:
    if(n % i == 0):
        count += 1
    if count > 2:
        break
    i += 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")