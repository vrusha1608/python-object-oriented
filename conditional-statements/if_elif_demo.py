# if elif demo program

marks = int(input("Enter your marks:"))

if(marks >= 90):
    grade = 'A'
elif(marks<90 and marks>=80):
    grade = 'B'
elif(marks<80 and marks>=70):
    grade = 'C'
else:
    grade = 'D'


print("Grade =>",grade)