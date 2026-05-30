try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))
    if amount>balance:
        print("Insufficient balance")
    else:
        print("Sufficient balance")
except:
    print("Error")
    
