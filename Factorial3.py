def iter_factorial(n):
    factorial=1
    n = input("Enter a number: ")
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
        return factorial
  
num=int(input("Enter the number: "))

print("factorial of ",num," (iterative): ",end="")
print(iter_factorial(num))
