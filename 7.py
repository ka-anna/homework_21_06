#Create a Python program that simulates a basic calculator.
#It should repeatedly ask the user for two numbers and an operator (+, -, *, /)
#and perform the corresponding operation using if/elif statements.
#Use a while loop to allow the user to perform multiple calculations until
#they choose to exit.
while 1:
 num1 = int(input("Enter first number:  "))
 num2 = int(input("Enter second number:  "))
 result = 0
 op = input("Enter operator +, -, *, /:  ")
 if op == "+":
    result = num1 + num2
 elif op == "-":
    result = num1 - num2
 elif op == "*":
    result = num1 * num2
 elif op == "/":
    result = num1 / num2
 else:
    print("Choose correct operator")
 print(result)

    
