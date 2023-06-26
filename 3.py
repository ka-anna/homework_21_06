#Implement a Python program that asks the user to enter a password.
#If the password matches a predefined secret password, display a success message.
#Otherwise, display an error message using an if/else ternary expression.
pw = input("Enter the password:  ")
rep = input("Reapit the password:  ")
if pw ==rep:
    print("Success")
else:
    print("Error")
