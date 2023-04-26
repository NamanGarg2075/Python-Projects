limit = int(input("Enter numbers of terms: "))

firstTerm = 1
difference = 1

result = (limit/2)*((2*firstTerm) + (limit -1)*difference)

if limit<=0:
    print("Terms can't be negative or zero")
else:
    print(f"Your sum of first {limit} natural number is: {result}")
