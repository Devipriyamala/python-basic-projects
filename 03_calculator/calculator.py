#Basic calculator system
first_number=int(input("enter a first number:"))
operator=input("enter a operator (+,-,*,/,//,%,**):")
second_number=int(input("enter a second number:"))

if operator=='+':
    result=first_number+second_number
    print(first_number,operator,second_number,"=",result)

elif operator=='-':
    result=first_number-second_number
    print(first_number,operator,second_number,"=",result)

elif operator=='*':
    result=first_number*second_number
    print(first_number,operator,second_number,"=",result)

elif operator=='/':
    if second_number==0:
        print("cannot be divide by zero")
    else:
        result=first_number/second_number
        print(first_number,operator,second_number,"=",result)

elif operator=='//':
    if second_number==0:
        print("cannot be divide by zero")
    else:
        result=first_number//second_number
        print(first_number,operator,second_number,"=",result)

elif operator=='%':
    if second_number==0:
        print("cannot be divide by zero")
    else:
        result=first_number%second_number
        print(first_number,operator,second_number,"=",result)

elif operator=='**':
    result=first_number**second_number
    print(first_number,operator,second_number,"=",result)

else:
    print("invalid operator")
