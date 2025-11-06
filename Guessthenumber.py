x=50
guess=None
attempts=0

while(x!=guess):
    guess=int(input("enter the guessing number: "))
    attempts+=1
    
    if(guess<x):
        print("Your Number is Lessthan Orginal Number...Try Again!!")
        print("Attempts",attempts)
    elif(guess>x):
        print("Your Number is Graterthan Orginal Number...Try Again!!")
        print("Attempts",attempts)
    else:
        print("Congratulations!! You Won The Game")
        print("Attempts",attempts)