import math as m 
#A painting company has determined that for every 112 square feet of wall space,
#one gallon of paint and eight hours of labor will be required.
#The company charges $35.00 per hour for labor.
#Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon.
#The program should display the following data:
#The number of gallons of paint required
#The hours of labor required
#The cost of the paint
#The labor charges
#The total cost of the paint job
#Include at least one function.

#ask for your inputs

wall = int(input("Enter the length of the wall in square feet: "))
paint_price = int(input("Enter the price of an paint bucket: "))

#do your calculations

def gallons(sqft):

   return m.ceil((sqft/112))

def labour(sqft):

   return (sqft / 112) * 8

def paint_cost():

   return paint_price * gallons(wall)

def labour_charge(sqft):

   return labour(sqft) * 35

def total(sqft):

   return paint_cost() + labour_charge(sqft)

#print required data

print(f"Number of Gallons of Paint Required: {gallons(wall)}")
print(f"The hours of labour required: {labour(wall):.2f} hours")
print(f"The cost of paint: ${paint_cost()}")
print(f"The labour charges: ${labour_charge(wall)}")
print(f"The Total Cost of the Job: ${round(total(wall), 2)}")