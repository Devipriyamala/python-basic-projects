# Even and Odd Counter
odd_count = 0
even_count = 0
for i in range(1,6):
  num = int(input(f"Enter number {i}: "))
  if num % 2 == 0:
    even_count += 1
  else:
    odd_count += 1
print("-----EVEN AND ODD COUNTER-----")
print("Even numbers: ",even_count)
print("Odd numbers: ",odd_count)
    
