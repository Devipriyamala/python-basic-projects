#Student Result System using if..elif..else 
name=input("Enter Student name:")
roll_no=int(input("Enter Student Roll no:"))
tamil=int(input("Enter Tamil mark:"))
english=int(input("Enter English mark:"))
maths=int(input("Enter Maths mark:"))
science=int(input("Enter Science mark:"))
social=int(input("Enter Social mark:"))
total=tamil+english+maths+science+social
average=total/5
print("-----STUDENT REPORT-----")
if average>=90:
    print("Name:",name)
    print("Roll no:",roll_no)
    print("Total Mark Scored:",total)
    print("Average:",average)
    print("Grade: A")
    print("Result: Pass")
elif average>=75:
    print("Name:",name)
    print("Roll no:",roll_no)
    print("Total Mark Scored:",total)
    print("Average:",average)
    print("Grade: B")
    print("Result: Pass")
elif average>=60:
    print("Name:",name)
    print("Roll no:",roll_no)
    print("Total Mark Scored:",total)
    print("Average:",average)
    print("Grade: C")
    print("Result: Pass")
elif average>=40:
    print("Name:",name)
    print("Roll no:",roll_no)
    print("Total Mark Scored:",total)
    print("Average:",average)
    print("Grade: D")
    print("Result: Pass")
else:
    print("Name:",name)
    print("Roll no:",roll_no)
    print("Total Mark Scored:",total)
    print("Average:",average)
    print("Grade: F")
    print("Result: Fail")



