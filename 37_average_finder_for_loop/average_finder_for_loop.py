# Calculate Average of 5 numbers
total = 0
average = 0
for i in range(1,6):
  num = int(input(f"Enter number {i}: "))
  total += num
average = total / 5
print("Total: ",total)
print("Average: ",average)
  
  
