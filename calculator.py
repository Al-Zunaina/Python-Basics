print('Calculator')
var='yes'
while var=='yes':
    print(' 1.Addition\n 2.Subtraction\n 3.Division\n 4.Multiplication')
    arith= int(input('Select one of the above options' ))
    num1=int(input('Enter the number'))
    num2=int(input('Enter the number'))
    if arith==1:
        print(num1+num2)
    elif arith==2:
        print(num1-num2)
    elif arith==3:
        print(num1/num2)
    elif arith==4:
        print(num1*num2)
    else:
        print('Invalid')
    var=input('if you wanna continue(yes/no)')

