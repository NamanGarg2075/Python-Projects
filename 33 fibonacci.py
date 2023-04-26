a = int(input("Enter your number: "))

def fibo(n):
    if (n ==0) or (n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2) 

for i in range(a):
    print(fibo(i))