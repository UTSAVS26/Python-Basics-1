l=[]
n=int(input("Enter Number of Elements: "))
for i in range(n):
     a = eval(input("Enter the elements: "))
     l.append(a)
print(l, "is your given list.")
x = int(input("""Enter the position of the
              element you want to delete: """))
l.pop(x)
y=int(input("Enter the number you want to add: "))
z=int(input("Enter the index number: "))
l.insert(z,y)
print(l, "is your final list.")
