print("~~~~~~~~~CALCULATOR~~~~~~~~~~")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Press 1 for Addition \
      Press 2 for Multiplication \
      Press 3 for division \
      Press 4 for sSubstraction")

choice = int(input("Enter value between 1-4: "))

match choice:
    case 1:
        print(f"Addition of {num1} and {num2} is {num1+num2}")
    case 2:
        print(f"Multiplication of {num1} and {num2} is {num1*num2}")
    case 3:
        print(f"Divison of {num1} and {num2} is {num1/num2}")
    case 4:
        print(f"Substraction of {num1} and {num2} is {num1-num2}")
    case _:
        print("INVALID VALUE!!!")
