# sum power to the digits of individual digits of number is equals to the number is an armstrong number

num = int(input("Enter your number: "))

sum = 0
numb = num
order = len(str(num))

while numb>0:
    digit = numb % 10
    sum += digit**order
    numb //= 10  # this will remove last digit

if sum == num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")