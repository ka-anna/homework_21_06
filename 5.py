#Write a Python function called find_common_elements that takes two lists as input
#and returns a new list containing the common elements between the two input lists.
#Use a for loop and an if statement to check for common elements.

#ls1 = input(list("Enter first list"))
#ls2 = input(list("Enter second list"))
ls1 = [1,2,3,4]
ls2 = [2,4,5,6, 11, 13, 2, 5,3]
comm_ls = []
for i in range (len(ls1)):
    for j in range (len(ls2)):
        if ls1[i]==ls2[j]:
            comm_ls.append(ls1[i])

print(list (set (comm_ls)))



