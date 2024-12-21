"""
Ask a user for a username and password. If the username is correct, check if
the password is correct, and display appropriate login messages
"""
correct_username = "rohitsharma"
correct_password = "sharmarohit"

username_data = input("Enter your username: ")


if username_data == correct_username:
    password_data= input("Enter your password: ")
    if password_data == correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")