# Count Positive, Negative, Zero 
positive_count = 0
negative_count = 0
zero_count = 0
for i in range(1,6):
  number = int(input(f"Enter number {i}: "))
  if number > 0:
    positive_count += 1
  elif number < 0:
    negative_count += 1
  else:
    zero_count += 1
print("Positive numbers: ",positive_count)
print("Negative numbers: ",negative_count)
print("Zeros: ",zero_count)

