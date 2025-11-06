# Another way: guessing game with limited attempts, no functions
import random
number_to_guess = random.randint(1, 10)
print("I am thinking of a number between 1 and 10. You have 5 tries.")
for attempt in range(5):
    guess = int(input("Guess the number: "))
    if guess == number_to_guess:
        print("You guessed it!")
        break
    elif guess < number_to_guess:
        print("Try a bigger number.")
    else:
        print("Try a smaller number.")
else:
    print(f"Sorry, the number was {number_to_guess}.")
# Simple number guessing game using basics
import random
number_to_guess = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
while True:
    guess = int(input("Guess the number: "))
    if guess == number_to_guess:
        print("You guessed it!")
        break
    elif guess < number_to_guess:
        print("Try a bigger number.")
    else:
        print("Try a smaller number.")
a = input("Enter a number: ")
temp = ""
n = len(a) - 1
while n >= 0:
    temp += a[n]
    n -= 1
print(temp)
if a == temp:
    print("Palindrome")
else:
    print("Not a palindrome")
#wap to guess the number 
#user will input number will multiple times
#input number is 10

