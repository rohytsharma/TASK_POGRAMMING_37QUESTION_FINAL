# 9. Accept the age of 4 people and display the oldest one
age_1 = int(input("Enter the age of person 1: "))
age_2 = int(input("Enter the age of person 2: "))
age_3 = int(input("Enter the age of person 3: "))
age_4= int(input("Enter the age of person 4: "))

oldest = max(age_1, age_2, age_3, age_4)
print(f"The oldest age is: {oldest}")
