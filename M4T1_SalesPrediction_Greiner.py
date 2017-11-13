#CTI-110
#M4T1-Sales Prediction
#Brett Greiner
#11/13/2017
#
#Get the projected total sales
total_sales = float(input('Enter Projected Sales:'))
#Calculate the profit as 23 percent of total sales.
profit=total_sales*0.23
#Display the profit
print('The profit is $', format(profit, ',.2f'))
