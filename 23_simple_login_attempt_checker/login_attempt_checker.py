#Simple Login Attempt Checker
user_name = input("Enter Username: ")
password = int(input("Enter Password: "))
if user_name == "admin" and password == 1234:
  print("Login Successful")
elif user_name != "admin" and password != 1234:
  print("Invalid Username and Incorrect Password")
elif user_name != "admin":
  print("Invalid Username")
elif password != 1234:
  print("Incorrect Password")
