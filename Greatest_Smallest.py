lst=[]
kst=[]
st=int(input("""How many numbers
             you want to enter: """))
n=st
for i in range(st):
     a=int(input("Enter Number: "))
     lst.append(a)
print("The List of %s Elements is: "%n,lst)
print("The Greatest Element is: ",max(lst))
print("The Smallest Element is: ",min(lst))
lst.sort(reverse=True)
print('The third largest number is',lst[2])
for k in range(st):
     b=int(input("Enter Number: "))
     kst.append(b)
print("The List of %d Elements is: "%n,kst)
mst=lst+kst
mst.sort(reverse=True)
print("The List of Final Elements is: ",mst)
