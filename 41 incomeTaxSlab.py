original_income = int(input("Enter your income: "))
taxable_income = original_income
tax = 0

if taxable_income <=300000:
    print("Income after tax: {}".format(original_income+tax))

else:
    taxable_income -=300000

# 3-6
    if taxable_income >= 300000:
        tax += 300000 * 5 / 100
        taxable_income -=300000
    # 6 - 9
        if taxable_income >= 300000:
            tax += 300000 * 10 / 100
            taxable_income -=300000
        # 9 - 12
            if taxable_income >= 300000:
                tax += 300000 * 15 / 100
                taxable_income -=300000
            # 12 - 15
                if taxable_income >= 300000:
                    tax += 300000 * 20 / 100
                    taxable_income -=300000
                # after 15
                    tax += taxable_income * 30/100
    
                else:
                    tax+= taxable_income *20/100
    
            else:
                tax+= taxable_income *15/100
    
        else:
            tax+= taxable_income *10/100
    
    else:
        tax+= taxable_income *5/100

# else:
#     taxable_income -=300000
#     tax += taxable_income * 5 / 100
#     # taxable_income -= 300000
#     # tax += taxable_income * 10 / 100

# print("Income after tax: {}".format(taxable_income))
print("Income after tax: {}".format(original_income+tax))
# elif income >= 300001:
#     if income <= 600000:
#         tax = income * 5 / 100
#     elif income >= 600001:
#         pass