marks=int(input('Enter the marks'))
if marks>35 or marks==35:
    print('True')
else:
    print('False')
#Teenager check
age=int(input('Enter the age'))
if age>13 and age<19:
    print('Teenagers')
else:
    print('Not teenagers')
#Divisibility check by 3 and 5
num=int(input('Enter the number'))
if num%3==0 or num%5==0:
    print('The number is divisible by 3 or 5')
else:
    print('The number is not divisible by 3 or 5')