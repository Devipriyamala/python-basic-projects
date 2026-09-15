name = input("Enter your name:")
amount = float(input("Enter your electricity bill amount:"))
print("-----ELECTRICITY BILL DISCOUNT CALCULATOR----")
print("Name: ",name)
print("Bill Amount: ",amount)
if amount >= 5000:
  print("Discount: 20%")
  total = amount-amount*(20/100)
  print("Final Amount: ",total)
elif amount >= 3000:
  print("Discount: 10%")
  total = amount-amount*(10/100)
  print("Final Amount: ",total) 
elif amount >= 1000:
  print("Discount: 5%")
  total = amount-amount*(5/100)
  print("Final Amount: ",total)
else:
  print(" No Discount")
  print("Final Amount: ",amount)
  
