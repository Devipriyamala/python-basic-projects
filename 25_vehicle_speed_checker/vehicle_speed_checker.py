#Vehicle Speed Checker
speed = int(input("Enter Vehicle Speed: "))
print("-----VEHICLE SPEED-----")
if speed <= 40:
  print("Result: Safe Speed")
elif speed <= 60:
  print("Result: Moderate Speed")
elif speed <=80:
  print("Result: High Speed")
elif speed > 80:
  print("Result: Over Speed")
  
  
