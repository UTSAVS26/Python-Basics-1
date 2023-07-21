# Program to display the month name and the number of days in that month
month_name = input("Input the name of Month: ")
if month_name == "February":
     year = int(input("Input the year: "))
     if ((year%400==0) or (year%4==0 and year%100!=0)):
          print("No. of days: 29 days")
     else:
          print ("No. of days: 28 days&quot;)
elif month_name in ("April","June","September","November"):
     print("No. of days: 30 days")
elif month_name in ("January","March","May","July","August","October","December"):
     print("No. of days: 31 days")
else:
     print("Wrong month name”)
