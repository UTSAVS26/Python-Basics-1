#Program to accept three numbers and show them in ascending order
A=int(input("Enter the value of A: "))
B=int(input("Enter the value of B: "))
C=int(input("Enter the value of C: "))
if(A<B and A<C) :
     smallest=A
     if(B<C):
          smaller=B
          small=C
     else:                            #B>=C
          smaller:C
          small:B
elif(B<A and B<C) :
     smallest=B
     if(C<A):
          smaller=C
          small=A
     else:                                   #C>=A
          smaller:A
          small:C
elif(C<A and C<B) :
     smallest=C
     if(A<B):
          smaller=A
          small=B
     else:                      #A>B
          smaller:B
          small:A
else:                             #A==C or A==B or B==C or A==B==C
     if (A==C) :
          if (B<A) :
               smallest =B
               smaller = small=C
          else:
               smallest = smaller =A
               small = B
     elif (A==B) :
          if (C<A) :
               smallest =C
               smaller = small=B
          else:
               smallest = smaller =A
               small = C
     elif (B==C) :
          if (A<C) :
               smallest =A
               smaller = small=B
          else:
               smallest = smaller =B
               small = A
     else:                            #A==B==C
          small = smaller = smallest= A
print ("Ascending Order = ",end=' ')
print(smallest , smaller , small , sep="<")
