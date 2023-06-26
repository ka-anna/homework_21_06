#Create a Python function called print_pattern that takes an integer as input
#and prints the following pattern using a while loop:
first = 1
ls =[]
value = int(input("Enter a number: "));
while value >= first:
 ls.append(first)
 print(ls)
 first= first+1
