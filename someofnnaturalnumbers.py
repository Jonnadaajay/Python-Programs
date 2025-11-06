# Program to calculate the sum of n positive numbers

n = int(input("Enter how many numbers you want to sum: "))
t = 0

for i in range(n):
    num = float(input(f"Enter positive number {i+1}: "))
    if num > 0:
        t += num
    else:
        print("Please enter a positive number.")

print(f"The sum of the {n} positive numbers is: {total}")