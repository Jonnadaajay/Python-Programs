num = int(input("Enter a number:"))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    i = 2
    is_prime = True
    while i <= int(num ** 0.5):
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")