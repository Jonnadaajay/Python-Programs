n=int(input("Enter a number:"))
if n < 2:
    print("It is not a prime number",+n)
else:
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
    