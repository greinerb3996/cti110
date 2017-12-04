# CTI-110 
# M6T2 - Bug Collector
# Brett Greiner 
# 12/03/2017



#Starting counter
total = 0

#Input how many bugs were collected each day
for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs


#Display total of bugs
print('You collected a total of', total, 'bugs.')
