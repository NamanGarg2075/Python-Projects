import re

def validate(inp):
    condition = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(condition,inp):
        return True
    else:
        return False
    
inp = input("Enter your email: ")

print(validate(inp))