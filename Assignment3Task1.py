f=int(input("Enter a number: "))
def factorial(n):
    a=1
    for i in range(1, n+1):
        a=a*i
    return a
r=factorial(f)
print(f"The factorial of {f} is: {r}.")        