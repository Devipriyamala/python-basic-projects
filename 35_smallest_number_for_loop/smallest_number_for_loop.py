# Finding Smallest number using for loop
number = int(input("Enter number 1: "))
smallest = number
for i in range (2,6):
  num = int(input(f"Enter number {i}: "))
  if num < smallest:
    smallest = num
print("Smallest number: ",smallest)
  
  
