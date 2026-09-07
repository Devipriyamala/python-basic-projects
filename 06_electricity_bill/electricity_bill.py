#Basic Electricity Bill calculation 

units = int(input("Enter your units: "))
if units <= 100:
    print("Rate per unit: 2 Rupees")
    total_bill = units * 2
    print("Total Bill:", total_bill)
elif units <= 200:
    print("Rate per unit: 3 Rupees")
    total_bill = units * 3
    print("Total Bill:", total_bill)
elif units > 200:
    print("Rate per unit: 5 Rupees")
    total_bill = units * 5
    print("Total Bill:", total_bill)
else:
    print("Enter a valid unit")
