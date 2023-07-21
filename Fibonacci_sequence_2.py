#Program to print Fibonacci Sequence.
nterms = int(input("How many terms you want to enter: "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("""Please enter a positive integer.
         Program Terminated!!!!!""")
elif nterms == 1:
   print("Fibonacci sequence upto ",nterms,":",end=" ")
   print(n1)
else:
   print("Fibonacci sequence upto %s: "%nterms)
   while count < nterms:
       print(n1,end="    ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
