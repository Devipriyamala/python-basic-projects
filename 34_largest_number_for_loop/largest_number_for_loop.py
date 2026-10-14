#Largest number using for loop
largest = int(input("Enter number 1: "))
for i in range(2,6):
  num = int(input(f"enter number {i}: "))
  if num > largest:
    largest = num
print("-----LARGEST NUMBER-----")
print("Largest number: ",largest)
    
  
    
  
  
