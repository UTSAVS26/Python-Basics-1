# Program to Calculate EMI.
def emi(p,r,n):
     r/=(12*100)
     n*=12
     EMI= (p*r*pow(1+r,n))//(pow(1+r,n)-1)
     return EMI
p=int(input("""Enter Value of Principal Amount
            (Primary Loan Amount): """))
r=int(input("""Enter Value of Rate of Interest
            per Year: """))
n=int(input("""Enter Value of Total Number
            of Years: """))
print("The Calculated EMI is: ",emi(p,r,n))
