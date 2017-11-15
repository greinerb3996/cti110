# CTI-110 
# M4HW2 - Tip Tax Total 
# Brett Greiner
# 11-15-17
#This calculates the total cost of a food purchase at a resuraunt
print('Input Food cost, sales tax, and tip amount')
foodCost = float(input('Food cost:'))
salesTax = .07 * foodCost
tipAmount = .18 * foodCost
print ('Total Cost:', (foodCost+salesTax+tipAmount))
