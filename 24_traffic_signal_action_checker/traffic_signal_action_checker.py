#Traffic Signal Action Checker
color = input("Enter traffic signal color: ")
print("-----TRAFFIC SIGNAL-----")
if color == "red":
  print("Action: Stop")
elif color == "yellow":
  print("Action: Get Ready")
elif color == "green":
  print("Action: Go")
else:
  print("Invalid Signal")
