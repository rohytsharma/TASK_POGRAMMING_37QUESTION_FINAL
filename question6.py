'''
WAP which accepts marks of four subjects and display total marks,
percentage and
grade.
Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
pass,
less than 40 –> fail
'''

data_1= int(input("Enter marks of Data Science: "))
data_2= int(input("Enter marks of Programming: "))
data_3= int(input("Enter marks of Software Design: "))
data_4= int(input("Enter marks of Maths"))

total_marks = data_1 + data_2 + data_3 + data_4

percentage = (total_marks / 400) * 100

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Division"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")