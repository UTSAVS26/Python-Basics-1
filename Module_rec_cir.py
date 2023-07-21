import circle
import rectangle
choice=0
ch="y"

while(ch=="y"):
     print("MENU")
     print("1. Area of a Circle.")
     print("2. Circumference of a Circle.")
     print("3. Area of a Rectangle.")
     print("4. Perimeter of a Rectangle.")
     print("5. Quit.")
     choice=int(input("Enter your choice: "))
     if choice==1:
          radius=int(input("Enter the Circle's radius: "))
          print("The area is : ",circle.area(radius))
     elif choice==2:
          radius=int(input("Enter the Circle's radius: "))
          print("The circumference is : ",circle.area(circumference))
     elif choice==3:
          width=int(input("Enter the Rectangle's width: "))
          length=int(input("Enter the Rectangle's length: "))
          print("The area is : ",rectangle.area(width,length))
     elif choice==4:
          width=int(input("Enter the Rectangle's width: "))
          length=int(input("Enter the Rectangle's length: "))
          print("The perimeter is : ",rectangle.perimeter(width,length))
     elif choice==5:
          print("Exiting the program....")
     else:
          print("Error: invalid selection.")
          import sys
          sys.exit()
