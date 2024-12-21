""""
Accept input from user
If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of
number
If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
 If given number is not multiple of 3 or 5 prints value as usual.
 """
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)