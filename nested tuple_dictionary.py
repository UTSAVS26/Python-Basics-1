a=('Name',('Rohit Sharma','Raman Arora'))
b=('Address',('Rohini','Ashok Vihar'))
c=('Fees',(2000,2300))
List=[a,b,c]
print("nested item of List ",List[0][1][0])
print("Item 2 of List ",List[1])
print("Item 3 of List ",List[2])

Studdict=dict(List)
print("Dictionary: ")
print(Studdict)
