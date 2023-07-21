dic = {}
while True:
    print("1. Add New Contact")
    print("2. Modify Phone Number of Contact")
    print("3. Display all entries")
    print("4. Check if a friend is present or not")
    print("5. Display in sorted order of names")
    print("6. Exit")
    inp = int(input("Enter your choice(1-6): "))
    if(inp == 1):
         n=int(input("Enter the Number of Entries: "))
         i=1
         while i<=n:
              name = input("Enter your friend name: ")
              phonenumber = input("Enter your friend's contact number: ")
              dic[name] = phonenumber
              i+=1
         print(dic)
         print("Contact Added \n")
    elif(inp == 2):
        name = input("Enter the name of friend whose number is to be modified: ")
        if(name in dic):
            phonenumber = input("Enter the new contact number: ")
            dic[name] = phonenumber
            print("Contact Modified\n")
        else:
            print("This friend's name is not present in the contact list\n")
    elif(inp == 3):
        print("All entries in the contact")
        for a in dic:
            print(a,"\t\t",dic[a])
        print("\n")
    elif(inp == 4):
        name = input("Enter the name of friend to search: ")
        if(name in dic):
            print("The friend",name,"is present in the list\n\n")
        else:
            print("The friend",name,"is not present in the list\n")
    elif(inp == 5):
        print("Name\t\t\tContact Number")
        for i in sorted(dic.keys()):
            print(i,"\t\t\t",dic[i])
            print("\n")
    elif(inp == 6):
        break
    else:
        print("Invalid Choice. Please try again")
        quit()
