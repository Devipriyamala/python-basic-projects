# Inverted Left Aligned Number Triangle
row = int(input("Enter the number of rows: "))
for i in range(row,0,-1):
  for j in range(row-i):
    print(" ",end = "")
  for k in range(1,i+1):
      print(k,end = "")
  print()
   
 
 
 
