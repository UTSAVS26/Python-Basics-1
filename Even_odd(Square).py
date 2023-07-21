# Program to print square if it is odd,
# otherwise print square root if it is even.
N=int(input("Enter  a number: "))
if (N%2==0) :
     import math
     print ("Square root of an even number: ",math.sqrt(N))
else :
     print ("Square of an odd number: ",N**2)
