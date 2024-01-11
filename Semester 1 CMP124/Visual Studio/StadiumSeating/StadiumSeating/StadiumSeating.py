def addtotal(count, price):
    total = count * price
    return total

classan = int(input("How many class A seats have been sold?"))
classbn = int(input("How many class B seats have been sold?"))
classcn = int(input("How many class C seats have been sold?"))

print(f'{classan} seats have been sold in class A, the total amount made is $', addtotal(classan, 20))
print(f'{classan} seats have been sold in class B, the total amount made is $', addtotal(classbn, 15))
print(f'{classan} seats have been sold in class C, the total amount made is $', addtotal(classcn, 10))
sum1 = addtotal(classan, 20)
sum2 = addtotal(classbn, 15)
sum3 = addtotal(classcn, 10)
print(f'The grandtotal is $', sum1 + sum2 + sum3)
