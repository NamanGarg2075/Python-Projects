lower = int(input("Enter lower limit: "))
upper = int(input("Enter uppwe limit: "))

for num in range(lower,upper+1):
    numb = num
    order = len(str(num))
    sum = 0
    while numb>0:
        digit = numb%10
        sum += digit**order
        numb//=10
    if sum==num:
        print(num)