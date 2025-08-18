'''purchase=int(input('Enyer the prize'))
coupon= input('Do you have a coupon(Y/N)')
if purchase>500:
    if coupon=='Y':
        print( purchase-purchase*0.1)
    else:
        print('No extra discount')
else:
   print('Purchase less than 500 no discount')'''
#Hotel Room Booking
ava=input('If room is available(Y/N)')
day=input('If it is weekend(Y/N)')
member=input('if a member(Y/N)')
if ava=='Y':
    print('Room available')
    if day=='Y':
        print('Weekend price')
        if member=='Y':
            print('10% ,discount')  
        else:
            print('No discount')
    else:
        print('Weekday price')
else:
    print('Room not available')

