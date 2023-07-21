# Program to convert octal numbers into decimal
print("Welcome to octal to decimal converter.")
n=int(input("Enter a octal number: "))
s,t=0,0
while n>0:
     d=n%10
     s=s+(d*(8**t))
     t=t+1
     n=n//10
print(s)
