cmd =''
result = int(input("Enter number: "))

while cmd.lower() != "=":
    print("--------CALCULATOR----------") 
    action = print('''For Addition Type (+)
For Substraction Type (-)
For Multiplication Type (*)
For Divide Type (/)
For Remainder Type (%)
For Calculation type (=)''')
    cmd = input()
    if cmd.lower() == "=":
        break
    number2 = int(input("Enter number: "))
    match cmd.upper():
        case '+':
            result += number2
        case '-':
            result -= number2
        case '*':
            result *= number2
        case '/':
            result /= number2
        case '%':
            result %= number2

print(result)