# Program to check the given year is leap year or not
input_year=int(input("Enter the year to be checked: "))
if(input_year%4==0):
     if(input_year%100==0):
          if (input_year%400==0):
               print("%d is leap year"%input_year)
          else:
               print("%d is not the leap year"%input_year)
     else:
          print("%d is leap year"%input_year)
else:
     print("%d is not the leap year"%input_year)
