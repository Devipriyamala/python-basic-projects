# Inverted pyramid star pattern using for loop
row = int(input("Enter the number of rows: "))
for i in range(row,0,-1):
  for j in range(row-i):
    print(" ",end = "")
  for k in range(i*2-1):
    print("*",end = "")
  print()
