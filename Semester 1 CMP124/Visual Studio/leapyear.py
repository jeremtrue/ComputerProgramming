#ask the user to input a year
currentyear = int(input("Enter a year: "))
#figure out weather the entered year is a leap year.
dfour = currentyear % 4
if int(dfour):
    print("The current year is not a leap year!")
    print("There is 28 days in Febuary.")
else:
    print("The current year is a leap year.")
    print("There are 29 days in Febuary.")