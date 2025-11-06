#atm
bal = 5000
a=9390
attempts = 3
while attempts > 0:
    a=int(input("enter the pin:"))
    if a==9390:
        print("welcome to SBI ATM")
        print("1.check balance")
        print("2.withdraw")
        print("3.deposit")
        print("4.exit")
    
        while True:
            choose=input("choose your operation:")
            if choose == "1":
                print(bal)
            elif choose =="2":
                amount =int(input("enter the amount to withdraw:"))
                if amount <= bal:
                    bal -= amount
                    print("withdrawn successfullu, balance is amount:",bal)
                else:
                    print("insufficient balance:",bal)
            elif choose=="3":
                amount =int(input("enter the amount to deposit:"))
                bal += amount
                print("deposit successfully, balance :",bal)
            elif choose=="4":
                print("thank you for using ATM")
                break
            else:
                print("invalid operation, please try again")
        break
    else:
        attempts -= 1
        print(f"invalid pin, you have {attempts} attempts left")
        if attempts == 0:
            print("your account is locked. Please contact the bank.")