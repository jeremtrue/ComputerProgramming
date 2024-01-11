#ask user for the temp in c
ctemp = float(input("Enter the tempurature in Celsius: "))
#do the conversion to farenheit
fract = ctemp * 9/5
farenheit = fract + 32
#print the f value
print(f'{ctemp} in farenheit is {farenheit}')
