'''Write a program to check whether a person is eligible for voting or not.
(accept age from user)'''
age_data= int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")