# Program to print not multiple of 3 using continue and break statements
for i in range (1,11):
     if (i%3==0):
          continue;
     if (i*3>25):
          break;
     print (i,end=" ")
else:
     print("Else part of loop")
print()
print(i)
