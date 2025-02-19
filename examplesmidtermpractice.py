print(type(2 + 3))
print(type(6 / 2))
print(type(2 != 3))
print(type(5 or 6))


print(2 + 3 * 5 ** 2)
print("hello" + " world")
print(3 * "abc")
print(True and False)




gross = int(input("Please enter your gross income: "))
children = (input("How many children do you have? "))
children = int(children)

if gross < 1000:
    tax = 0.1
elif gross < 2000:
    tax = 0.12
elif gross < 4000:
    tax = 0.14
else:
    tax = 0.18

if gross < 2000:
    tax_cut = children * 0.01
else:
    tax_cut = children * 0.005

effective_tax_rate = max(0, tax - tax_cut)


net_salary = gross * (1 - effective_tax_rate)

print(f"Your net salary is: {net_salary:.2f}")
print("Invalid input. Please enter numeric values for gross salary and number of children.")



