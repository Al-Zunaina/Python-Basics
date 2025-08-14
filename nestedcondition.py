age=int(input('Enter the age'))
if age>=18:
    if age>=50:
        print('Submit a medical vertificate')
    else:
        print('Eligible for driving')
else:
    if age<=5:
        print('a baby')
    else:
        print('can not drive')
    