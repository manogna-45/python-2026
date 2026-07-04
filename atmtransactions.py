balance = 5000
transactions = 0
while True:
    print("   ATM   ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    password = 1212
    pin = int(input("Enter PIN: "))
    if pin == password:
        print("Welcome!")
    else:
        print("Wrong PIN")
        break
    if choice == 1:
        print("Balance: ", balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        amount += balance
        transactions += 1
        print("Deposited Successfully!")
        print("Current Balance: ", balance) 
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            amount -= balance
            transactions += 1
            print("Withdrawed Successfully!")
            print("Current Balance: ", balance)    
        else:
            print("Insufficent Balance!")
    elif choice == 4:
        print("Thank you for visiting!")
        print("Transactions: ", transactions)
        break
    else:
        print("Invalid Choice!")          
