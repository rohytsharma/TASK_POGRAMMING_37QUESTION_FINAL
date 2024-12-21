"""
Write a program to whether a number (accepted from user) is divisible by 2
and 3 both.
"""
num_data = int(input("Enter a number: "))
if (num_data % 2 == 0 and num_data % 3 == 0):
    print(f"{num_data} is divisible by both 2 and 3.")
else:
    print(f"{num_data} is not divisible by both 2 and 3.")