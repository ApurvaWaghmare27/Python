# If elif else ladder

# age = int(input("Enter your age: "))

# if(age >= 18):
#     print("You can vote!!!")
# elif(age == 0):
#     print("You are entering 0 which is invalid...")
# elif(age < 0):
#     print("Invalid age...")
# else:
#     print("Your age is less than 18...")

print("End of program")


# a = int(input("Enter a number: "))
# if(a%2 == 0):
#     print("The number is even...")
# else:
#     print("The number is odd...")

marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)
