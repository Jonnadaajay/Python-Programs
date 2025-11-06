#atm
bal = 5000
pin = 1234

entered_pin = int(input("Enter the PIN:"))
if entered_pin == pin:
    print("Welcome to SBI ATM")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Set PIN")
    print("5. Exit")
    
    while True:
        choose = input("Choose your operation:")
        if choose == "1":
            print("Balance:", bal)
        elif choose == "2":
            amount = int(input("Enter the amount to withdraw:"))
            if amount <= bal:
                bal -= amount
                print("Withdrawn successfully, balance is:", bal)
            else:
                print("Insufficient balance:", bal)
        elif choose == "3":
            amount = int(input("Enter the amount to deposit:"))
            bal += amount
            print("Deposit successful, balance:", bal)
        elif choose == "4":
            new_pin = int(input("Enter new PIN:"))
            pin = new_pin
            print("PIN set successfully!")
        elif choose == "5":
            print("Please collect your card")
            print("Thank you for using ATM")
            print("Have a nice day!")
            break
        else:
            print("Invalid operation, please try again")
else:
    print("Invalid PIN, please check your PIN")