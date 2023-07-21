n=int(input("Enter a decimal number: "))
a=[]
while(n>0):
    dig=n%8
    a.append(dig)
    n=n//8
a.reverse()
for i in a:
    print(i,end="")
