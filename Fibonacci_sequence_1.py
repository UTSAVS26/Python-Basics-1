#Python program to print the Fibonacci Sequence
nterms=int(input("How many terms? "))

#first two numbers
n1,n2=0,1
count=0

# check if the number of terms is valid
#    0    1    1    2    3    5    8    13   21
if nterms <=0:
     print("Please enter a positive integer")
elif nterms ==1:
     print("Fibonacci sequence upto",nterms,":")
     print(n1)
else:
     print("Fibonacci sequence: ")
     while count<=nterms:
          print(n1)
          nth=n1+n2
          # update values
          n1=n2
          n2=nth
          count+=1    #count=count+1
