# Using 3rd variable
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num3 = num1
num1 = num2
num2 = num3

print(f"Your first number is {num1} and second number is {num2}")

# without using 3rd variable
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1,num2 = num2,num1 # this will interchange values

print(f"Your first number is {num1} and second number is {num2}")