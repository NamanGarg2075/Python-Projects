terms = int(input("Enter number of terms: "))

result = list(map(lambda x: 2**x,range(terms+1)))

# print(result)

for i in range(terms+1):
    print(f"Value of 2 power {i} is {result[i]}")