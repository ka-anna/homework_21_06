#Write a Python pr
#ogram that prints
#all the prime numbers between 1 and 100 using a for loop and the break keyword.
#if first_v < 100:
for i in range(1, 100):
 for j in range (2, i):
  if (i % j) == 0:
   break
 else:
  print(i)

   
    
