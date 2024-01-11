
'''
Write a program that calculates the amount of money a person
would earn over a period of time if their salary is one penny the
first day, and continues to double each day. the program should 
ask the user for the number of days. Display a table showing what
the salary was for each day, then show the total pay at the end of
the period. The output should be displayed in a dollar amount, not
the number of pennies.

'''

#init var
numofday = int(input("Enter a number of days: "))
totalpay = 0
sal = 1

#do the operation

for count in range(1,numofday +1):
    change = sal /100
    print(f'Day: {count}\t\t${change:,.2f}')
    totalpay += sal
    sal += sal

#print the totals

finaltotal = totalpay / 100
print(f'Your total pay is ${finaltotal}.')