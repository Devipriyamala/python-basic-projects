# Movie Ticket Booking System using Conditional statements 

age = int(input("Enter your age:"))
tickets = int(input("Enter number of tickets:"))
if age >= 60:
    price = 80
    total = price * tickets
elif age >= 18:
    price = 150
    total = price * tickets
elif age >= 5:
    price = 100
    total = price * tickets
else:
    price = 0
    total = 0
print("-----MOVIE TICKET-----")
print("Age:", age)
print("Tickets:", tickets)

if age < 5:
    print("Free Ticket")
else:
    print("Ticket Price:", price)
    print("Total Amount:", total)
