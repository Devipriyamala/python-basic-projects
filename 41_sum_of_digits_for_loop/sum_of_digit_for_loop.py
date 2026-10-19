# Sum of the digits
total = 0
number = input("Enter a positive whole number: ")
if number.isdigit() and int(number) > 0:
  for i in number:
    digit = int(i)
    total = digit + total
  print(total)
else:
  print("Invalid input.Please enter a valid positive whole number.")
