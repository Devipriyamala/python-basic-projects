# Project 4: ATM System

print("----- ATM SYSTEM -----")

entered_pin = int(input("Enter the PIN: "))
correct_pin = 1234
account_balance = 10000

if entered_pin == correct_pin:
    withdrawal = int(input("Enter withdrawal amount: "))

    if withdrawal > account_balance:
        print("Insufficient Balance")
    else:
        remaining_balance = account_balance - withdrawal
        print(f"Withdrawal Amount : {withdrawal}")
        print(f"Remaining Balance : {remaining_balance}")
        print("Transaction Successful")
else:
    print("Invalid PIN")
