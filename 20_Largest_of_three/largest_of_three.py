#Largest of Three Numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
print("-----LARGEST NUMBER CHECKER-----")
print("First number:",num1)
print("Second number:",num2)
print("Third number:",num3)
if num1 == num2 == num3:
  print("Result: All the three numbers are equal")
elif num1 >= num2 and num1 >= num3:
  print("Result:",num1,"is the largest number")
elif num2 >= num1 and num2 >= num3:
  print("Result:",num2,"is the largest number")
else:
  print("Result:",num3,"is the largest number")
