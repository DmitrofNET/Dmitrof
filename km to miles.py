while True:
    try:
        km = float(input("Enter A Value For KM:\n"))
    except:
        print('Please enter a didgit')
    else:
        total = km*0.621371
        total2 = km/1.609

        print(f"{km} km = {total} or {total2} miles")
        print('_'*50)
        break


    print ('Meters to Milimeters')
while True:
    try:
        m = float(input('Enter a value for Meters:\n'))
            
    except:
        print('Please enter a didgit')
    else:
        totalm = m*100

        print (f'{m} meters = {totalm} Milimeters')
        break

