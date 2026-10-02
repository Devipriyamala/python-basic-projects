#Triangle Checker
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
  if side1 == side2 == side3:
    print("Result: Equilateral Triangle")
  elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Result: Isosceles Triangle")
  else:
    print("Result: Scalene Triangle")
else:
  print("Result: Not a valid Triangle")
  
    

