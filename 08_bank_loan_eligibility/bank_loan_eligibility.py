#Bank Loan Eligibility using nested if
age = int(input("Enter your Age: "))
salary = int(input("Enter your Monthly Salary: "))
score = float(input("Enter your Credit Score: "))
if age >= 18:
  if salary >= 25000:
    if score >= 700:
      print("Loan Eligible")
    else:
      print("Loan Rejected: Low Credit Score")
  else:
    print("Loan Rejected: Low Salary")
else:
  print("Loan Rejected: Age Requirement Not Met")
  
