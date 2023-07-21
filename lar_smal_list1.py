# Program to find largest and smallest number in a list
Num = list()               # An empty set
print("How many numbers you want to enter: ",end=" ")
N= int(input())
Ctr=1
if N>0:
     while Ctr<=N:
          print("Enter No.:",Ctr,end="->")
          Val=int(input())
          Num.append(Val)           # adding into list
          Ctr+=1

# Initialize the default value to max and min
MaxN=Num[0]             # Assume that the first list value is the maximum number
MinN=Num[0]              # Assume that the first list value is the minimum number
for i in range(len(Num)):
     if (Num[i]>MaxN):
          MaxN=Num[i]
     if (Num[i]<MinN):
          MinN=Num[i]
print("The maximum value in the list is ",MaxN)
print("The minimum value in the list is ",MinN)
