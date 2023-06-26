#Implement a Python function called find_factorial that takes a positive
#integer as input and calculates its factorial using
#a while loop. Use the pass keyword to handle the case when the input is zero.
value = int(input("Enter a number: "));
factorial=1;
if value < 0:
    print ("Error")
while value > 0:
    factorial = factorial * value;
    value = value -1;
print(factorial)
if value == 0:
    pass
