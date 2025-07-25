"""a=10
a+=10
print(a)
a=a*5
print(a)"""

"""a="Harish"
b="s" in a
print(b)

a=[1,2,3,4,5]
b=4 in a
print(b)
b=5 not in a
print(b)"""

"""a=10
b=10
print(id(a))
print(id(b))
print(a is b)

a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)"""


"""Student_id = 505
Student_name = "Harish"
Student_age = 21
Quiz_score = 78
Assignment_score = 80
Exam_score = 85
Student_attendance = 90

Total_score = Quiz_score + Assignment_score + Exam_score

Average_score = Total_score/3

Student_passed = Average_score >= 75

Student_attendance += 1

Student_award = Student_attendance >= 90 and Student_passed

print(Student_id)
print(Student_name)
print(Student_age)
print(Quiz_score)
print(Assignment_score)
print(Exam_score)
print(Total_score)
print(Average_score)
print(Student_attendance)
print(f"Student passed : {Student_passed}")
print(f"Award Eligibility : {Student_award}")"""

#if statement
"""num=12
if num>=10 and num<=20:
    print(f"{num} is there")"""
#conditional operators using if-else statements
"""value = -10
if value<0:
    print(f"Given {value} is Negative")
else:
    print(f"Given {value} is Positive")"""

"""email = input("Enter your email : ")
print(f"Welcome:{email}")"""

#Ternary operator using if-else statements
"""email=input("Enter your email : ")
age=int(input("Enter your age : "))
status="you can vote" if age>=18 else "you cannot vote"
print(status)"""

"""choice = int(input("Enter your choice"))
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Invalid")"""

#Nested conditions
age=22
has_id=True

if age>=21:
    if has_id:
        print("Allow to enter")
    else:
        print("To show Id to enter")
else:
    print("you are too young to enter")