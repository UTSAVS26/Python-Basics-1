#Program to Find the Smallest from N Numbers.
lst=[]
n=int(input("Enter Limit: "))
for i in range(n):
     a=int(input("Enter %sst Number: "%(i+1)))
     lst.append(a)
print("The Numbers You Entered are: ",lst)
print("The Greatest Number is: ",min(lst))
