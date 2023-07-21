#Python program to find the factorial of a number input by the user
num=int(input("Enter a number :"))
if num<0:
     print("Sorry, factorial of negative number",num,"is not exist")
elif num==0:
     print(" The factorial of 0 is 1")
else:
     factorial=1
     for i in range(1,num+1):
          factorial*=i
     print("The factorial of",num,"is",factorial)
