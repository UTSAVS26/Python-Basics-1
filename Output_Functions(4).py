def call(n1 = 2, n2 = 4):
     n1 = n1 * n2
     n2 += 2
     print(n1, n2)
call()
call(5, 10)
call(10)
print(end='\n')

def greet(*names):
     for I in names:
          print("Hello", I)
greet("Nitin", "Mrinal", "Anil")
print(end='\n')


def Change(P ,Q=30):
     P=P+Q
     Q=P-Q
     print( P,"#",Q)
     return (P)
R=150
S=100
R=Change(R,S)
print(R,"#",S)
S=Change(S)
print(end='\n')

def Changer(P,Q=10):
     P=P/Q
     Q=P%Q
     print (P,"#",Q )
     return P
A=200
B=20
A=Changer(A,B)
print (A,"$",B )
B=Changer(B)
print (A,"$",B)
A=Changer(A)
print (A,"$",B )
