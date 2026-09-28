#Largest of Two Numbers
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
print("-----Largest Number Checker-----")
print("First Number:",num1)
print("Second Number:",num2)
if num1 > num2:
  print("Result:",num1,"is the largest number")
elif num1 < num2:
  print("Result:",num2,"is the largest number")
else:
  print("Result: Both numbers are equal")
