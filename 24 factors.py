num = int(input("Enter your number: "))

factors=[]

for i in range(1,num+1):
    if (num%i==0):
        factors.append(i) # we can also simple print this value but you know haha...

print(f"Factrs of {num} is {factors}")