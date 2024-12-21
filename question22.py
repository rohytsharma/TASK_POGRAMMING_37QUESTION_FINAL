"""
Write a program to accept percentage and display the category according to
the following criteria:
Percentage Category
<40 Failed
>=40 and <55 Fair
>=55 and <65 Good
>=65 Excellent
"""

percentage_data = float(input("Enter your percentage: "))
if percentage_data < 40:
    category_data = "Failed"
elif 40 <= percentage_data < 55:
    category_data = "Fair"
elif 55 <= percentage_data < 65:
    category_data = "Good"
elif percentage_data >= 65 and percentage_data <=100:
    category_data = "Excellent"
else:
    category_data = "Invalid percentage"
print(f"Your category is: {category_data}")