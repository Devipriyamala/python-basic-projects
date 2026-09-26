#Leap Year Checker

year = int(input("Enter a Year: "))
print("-----LEAP YEAR CHECKER-----")
print("Year: ",year)
if (year % 400 == 0):
  print("Result: Leap Year")
elif (year % 4 ==0) and (year % 100 != 0):
  print("Result: Leap Year")
else:
  print("Result: Not Leap Year")
