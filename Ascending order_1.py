#Program to accept three numbers and show them in ascending order
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
if(b>a):
     a,b=b,a
if(c>b):
     c,b=b,c
     if(a>b):
          b,a=a,b
print(a,b,c)
