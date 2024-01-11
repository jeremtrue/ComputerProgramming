#ask neccessary questins
r = float(input("What is the length of the row in feet: "))
e = float(input("What is the space used by the end post in feet; "))
s = float(input("What is the amount of space between vines in feet: "))
#CALCULATE
v = int((r - (2 * e)) / s)
print(f'{v} is how many grapevines fit in the row.')