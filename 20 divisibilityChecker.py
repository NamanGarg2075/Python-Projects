num1 = float(input("Enter number you want to divide: "))
num2 = float(input("Enter number you want to divide by: "))

if num1%num2==0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")