"""
N students take K apples and distribute them among each other evenly. The
remaining (the indivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket? The
program reads the numbers N and K. It should print the two answers for the
questions above.
"""
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

apples_per_student = K // N
remaining_apples = K % N

print(f"Each student gets {apples_per_student} apples.")
print(f"{remaining_apples} apples remain in the basket.")