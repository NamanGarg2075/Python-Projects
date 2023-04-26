num = int(input("Enter number: "))
b = num
a=num
num = num - (num-1)

while a>0:
    for i in range(1,num+1):
        print(i, end=" ")
    num+=1
    if a == 1:
        num = b-1
        while range(1,num+1):
            print(num, end=" ")
            num-=1
    else:   
        print()
    a-=1
    
print()


num = b
# num = num - (num-1)

while num>0:
    for i in range(1,num):
        print(i, end=" ")
    num-=1
    print()