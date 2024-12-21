'''
Accept the grades from the user and display the grade according to the
following criteria:
Below 25 --D
25 to 45 -- C
45 to 50 -- B
50 to 60 --B+
60 to 80 -- A
Above 80 -- A
'''
marks_data = float(input("Enter your marks: "))

if marks < 25:
    grade = "D"
elif 25 <= marks_data <= 45:
    grade = "C"
elif 45 < marks_data <= 50:
    grade = "B"
elif 50 < marks_data<= 60:
    grade = "B+"
elif 60 < marks_data<= 80:
    grade = "A"
else:
    grade = "A+"


print(f"Your grade is: {grade}")