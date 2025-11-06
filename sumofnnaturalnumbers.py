# Program to check if a number is prime
num = int(input("Enter a number to check if it is prime: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
# Sum of n positive numbers using a while loop

n = int(input("Enter how many numbers to sum: "))
count = 0
total = 0

while count < n:
    num = float(input(f"Enter positive number {count+1}: "))
    if num > 0:
        total += num
        count += 1
    else:
        print("Please enter a positive number.")

print(f"The sum of the {n} positive numbers is: {total}")