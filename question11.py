'''
A company decided to give bonus to employee according to following
criteria:
Time period of service Bonus
More than 10 years 10%
>=6 and <=10 8%
Less than 6 years 5%
'''
years_of_service_data = int(input("Enter the number of years of service: "))
salary_data = float(input("Enter the employee's salary: "))

if years_of_service_data > 10:
    bonus = salary_data * 0.10
elif 6 <= years_of_service_data <= 10:
    bonus = salary * 0.08
else:
    bonus = salary_data * 0.05

# Display the bonus amount
print(f"The bonus amount is: Rs {bonus:.2f}")