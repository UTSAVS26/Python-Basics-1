d={}
years=[]
month=[]
n=int(input("How many records"))

# Creating list of years and month
for i in range(0,n):
     m=int(input("Enter year "))
     n=int(input("Enter month "))
     years.append(m)
     month.append(n)

# Adding List in Dictionary
d["year"]=years
d["month"]=month

print(d)
