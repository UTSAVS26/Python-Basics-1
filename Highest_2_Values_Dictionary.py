dic = {}
n=int(input("""Enter Number of Items
You Want to Add in a Dictionary: """))
for i in range(n):
     m=input("Enter Key: ")
     n=(input("Enter Value: "))
     dic[m]=n
print("The Dictionary is: ",dic)
lst = list()
for a in dic.values():
    lst.append(a)
lst.sort()
print("Highest value:",lst[-1])
print("Second highest value:",lst[-2])
