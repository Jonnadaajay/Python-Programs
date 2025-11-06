n = int(input("Enter a number:"))
if n < 0:
    result = "Factorial not defined for negative numbers"
elif n == 0 or n == 1:
    result = 1
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
print("Factorial of", n, "is:", result) 