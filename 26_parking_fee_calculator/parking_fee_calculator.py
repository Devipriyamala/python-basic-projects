#Parking Fee Calculator
hour = int(input("Enter Parking Hours: "))
print("-----PARKING FEE-----")
if hour <= 2:
  print("Parking Fee: 30 rupees")
elif hour <= 5:
  print("Parking Fee: 50 rupees")
elif hour <= 8:
  print("Parking Fee: 80 rupees")
else:
  print("Parking Fee: 120 rupees")
  
