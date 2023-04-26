value = float(input("Enter your value: "))
units = input("Enter it's unit (k or l): ")

if units=="k":
    ans = value / 1.609
    unit = "Miles"
else:
    ans = value * 1.609
    unit = "Kilo"

print(f"{value} {units} equals {ans} {unit}")