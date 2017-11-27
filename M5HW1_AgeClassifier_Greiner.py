# CTI-110 
# M5HW1 - Age Classifier 
# Brett Greiner 
# 11/26/2017
#
def main():
    print ('Age Bracket Calculator')    
main()
age = int(input('Enter an age: '))
#What age defines what age bracket
if age <= 1:
    print('He or She is an infant')
if age >= 1 and age <=12:
    print('He or She is a child')
if age >=13 and age <=19:
    print('He or She is a teenager')
if age >=20:
    print('He or She is an adult')


        
