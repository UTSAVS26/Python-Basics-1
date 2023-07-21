# Program to Store 5 Users Along with Password in a Dictionary.
# Check Whether the User is Authorized User or Not.
d1=dict()
i=1
n=int(input("Enter Number of Entries: "))
while i<=n:
     user_name=input("Enter Username: ")
     password=input("Enter Password: ")
     d1[user_name]=password
     i+=1
print("Dictionary for Username and Password: ",d1)
l=d1.keys()
m=d1.values()
print("\nUSERNAME\t\t","PASSWORD\t\t")
for i in l:
     z=d1[i]
     print("\n",i,"\t\t",end=" ")
     for j in z:
          print(j,end="")
x=input("""\n\nEnter Username to be
Checked if it is Authorized or Not: """)
y=input("Enter Password to be Verification: ")
if x in l:
     if y in m:
          print("The User is Authorized.")
     elif y not in m:
          print("The User is not Authorized.")
elif x not in l:
     print("The User is not Authorized.")
