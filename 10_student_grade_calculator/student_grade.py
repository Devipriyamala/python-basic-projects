#student grade calculator using conditional statements
name = input("enter your name:")
mark = int(input("enter your mark:"))
print("-----STUDENT GRADE-----")
print("Name: ",name)
print("Mark: ",mark)
if mark>=90:
    print("Grade: A Grade")
elif mark>=75:
    print("Grade: B Grade")
elif mark>=60:
    print("Grade: C Grade")
elif mark>=40:
    print("Grade: D Grade")
else:
    print("Grade: Fail")
