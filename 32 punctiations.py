punc = '''!@#$%^&*()-_=+{}[]\|/?.>,<`~;:'''

string = input("Enter anything here: ")
emptyString = ""

for i in string:
    if i not in punc:
        emptyString+=i

print(emptyString)