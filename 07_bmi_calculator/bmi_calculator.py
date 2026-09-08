#Basic BMI Calculator
weight = float(input("Enter your weight(in kgs):"))
height = float(input("Enter your height(in meters):"))
BMI = weight/(height*height)
print("BMI :", round(BMI,2))
if BMI < 18.5:
  print("BMI Category is Underweight")
elif BMI >= 18.5 and BMI <=24.9:
  print("BMI Category is Normal weight")
elif BMI >=25 and BMI <=29.9:
  print("BMI Category is Overweight")
else:
    print("BMI Category is Obese")
  
  
