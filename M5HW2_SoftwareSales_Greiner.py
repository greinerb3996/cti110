# CTI-110 
# M5HW2 - Software Sales
# Brett Greiner 
# 11/26/2017
#
def main():
    print ('Discount percentage by purchase amount')
packageCost = 99
quantity = float(input('Enter quantity: '))
discount10 = .10
discount20 = .20
discount30 = .30
discount40 = .40
beforeDiscount = packageCost * quantity
main()
#Discount off purchased amount of software
if quantity == 0 and quantity <= 9:
    print ('You do not currently recieve a discount')
if quantity >= 10 and quantity <= 19:
    print('You recieve a 10% discount')
if quantity >= 20 and quantity <=49:
    print('You recieve a 20% discount')
if quantity >=50 and quantity <=99:
    print('You recieve a 30% discount')
if quantity >=100:
    print('You recieve a 40% discount')
totalCost = beforeDiscount 
print ('Total Cost:')

        
