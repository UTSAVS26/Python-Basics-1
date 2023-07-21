n=int(input("Enter the decimal value: "))
bs=' '
while n!=0:
     r=n%16
     if int(r)==10:
          bs+='A'
     elif int(r)==11:
          bs+='B'
     elif int(r)==12:
          bs+='C'
     elif int(r)==13:
          bs+='D'
     elif int(r)==14:
          bs+='E'
     elif int(r)==15:
          bs+='F'
     else:
          bs+=str(r)
     n//=16
print("Decimal Equal Hexadecimal Number is: ")
for i in range(len(bs)-1,-1,-1):
     print(bs[i],end='')
