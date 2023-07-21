n=int(input("Enter a binary number: "))
s,t=0,0
while n>0:
     d=n%10
     s+=(d*(2**t))
     t+=1
     n//=10
print(s)
