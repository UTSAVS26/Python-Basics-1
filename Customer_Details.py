n = int(input("Enter the number of customers to be entered: "))
cst_dict = dict()
print()
for i in range(n):
     x = input("Enter the name of the customer: ")
     y = input("Enter the product purchased: ")
     z = input("Enter the phone number of the customer: ")
     u = input("Enter the cost of product purchased: ")
     cst_dict[x] = y, z, u
     print()
print()
print("This is your given dictionary: ")
print("Name", "\t\t", "Product Purchased", "\t\t","Cost", "\t\t" "Phone Number")
for i in cst_dict:
     print(i, "\t\t\t", cst_dict[i][0], "\t\t\t", cst_dict[i][1], "\t\t\t", cst_dict[i][2])

