num = int(input("Enter your number: "))

def factorial(n):
    if (n == 0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(num))
