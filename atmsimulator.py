pin=3456
amount=9000
var=int(input('Enter the pin'))
if var==pin:
    print('login successful')
    while True:
        print('=========ATM==========')
        print(' 1.Check Balance\n 2.Deposit\n 3.Withdraw\n 4.Exit')
        en=int(input('Enter the choice'))
        if en==1:
            print(f'The balance is ${amount}')
        elif en==2:
            depo=int(input('Enter thr deposit amount'))
            print(f'${depo} has been deposited')
            amount=depo+amount
        elif en==3:
            wit=int(input('Enter the amount to be withdrawn'))
            print(f'${wit} have been withdrawn')
            amount=amount-wit
        elif en==4:
            print('Exited')
            break
            


else:
    print('falied login')
