#decalre variables
monthlyloss = 4
intakestart = 500
#ask the questin
startweight = int(input("What is your weight?"))
#do more variables
months = 12
passedmonths = 0
currentweight = startweight
#do yours calculationshsshs
while months > 0:
    currentweight -= 4
    passedmonths += 1
    #PRINT
    print(f'Your weight after {passedmonths} months is {currentweight}.')
    months -= 1
