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
"""age=22
has_id=True

if age>=21:
    if has_id:
        print("Allow to enter")
    else:
        print("To show Id to enter")
else:
    print("you are too young to enter")"""

#while loop
"""password = "Harish123"
user_input = ""
while password != user_input:
    user_input = input("Enter Password : ")
print("Access Granted")"""

#for loop
"""for i in range(1,20):
    if i%2==0:
        print(i,end=" ")"""

"""count=2
while count<=20:
    print(count)
    count+=2"""

"""for i in range(2,20,2):
    print(i)"""

"""for i in range(1,4):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")"""

"""i=1
while i<=3:
    j=1
    while j<=10:
        print(f"{i} X {j} = {i*j}")
        j+=1
    i+=1"""

"""import random

otp=random.randint(0000,9999)
print(otp)

attempts = 3
while attempts:
    user_otp = int(input("Enter otp : "))
    if len(str(user_otp)) != 4:
        print("OTP Must be 4 digit number only")
    if user_otp == otp:
        print("Correct OTP - Success")
        break
    attempts -= 1
else:
    print("Maximum attempts done, try after 24 hours")"""

# Input student details
"""student_id = input("Enter Your ID: ")
student_name = input("Enter Your Name: ")

# Initialize variables
total_score = 0
subject_count = 0

# Loop to collect subject scores
while True:
    score = int(input("\nEnter score for Subject " + str(subject_count + 1) + ": "))
    total_score = total_score + score
    subject_count = subject_count + 1

    another = input("Do you want to enter another score? (yes/no): ")
    if another != "yes":
        break

# Set attendance (fixed as per image)
attendance = 50.0

# Calculate average
average_score = total_score / subject_count

# Determine performance using if conditions
if average_score >= 85:
    performance = "Excellent"
else:
    if average_score >= 70:
        performance = "Good"
    else:
        if average_score >= 50:
            performance = "Average"
        else:
            performance = "Poor"

# Attendance status
if attendance < 75:
    attendance_status = "WARNING - Low Attendance"
else:
    attendance_status = "Satisfactory Attendance"

# Output results
print("\n======== Student Details ========")
print("Student ID:", student_id)
print("Student Name:", student_name)
print("Student Attendance:", str(attendance) + "%")
print("Total Score:", total_score)
print("Total Number Of Subjects:", subject_count)
print("Average Score:", round(average_score, 1))
print("Performance:", performance)
print("Attendance:", attendance_status)"""

a="python"
print(a[-5:-1])
