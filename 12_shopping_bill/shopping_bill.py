#Basic Shopping Bill Calculator

item_name = input("Enter Item Name: ")
price = float(input("Enter price of one Item: "))
quantity = int(input("Enter quantity needed: "))
amount = price * quantity
print("-----SHOPPING BILL-----")
print("Item: ",item_name)
print("Price: ",price)
print("Quantity: ",quantity)
print("Total Amount: ",amount)
