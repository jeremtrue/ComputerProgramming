#ask for the cost of each item
purchase1 = float(input("Price of Item 1:"))
purchase2 = float(input("Price of Item 2:"))
purchase3 = float(input("Price of Item 3:"))
purchase4 = float(input("Price of Item 4:"))
purchase5 = float(input("Price of Item 5:"))
#calculate subtotal, tax, total
subtotal = (purchase1 + purchase2 + purchase3 + purchase4 + purchase5)
tax = subtotal * 0.07
total = subtotal + tax

#print subtotal, tax, total
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')