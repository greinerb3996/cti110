#CTI 110
#M7T1 - Kilometer Converter
#Brett Greiner
#12/04/2017

CONVERSION_FACTOR = 0.6214
def main():
    #Get distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))
    #Display the distance converted to miles.
    show_miles(kilometers)
def show_miles(km):
    #Calculate miles
    miles = km * CONVERSION_FACTOR
    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

main()
