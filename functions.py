#defining a function
def funct1(ms1,ms2):
    print(ms1,ms2)
   
#calling a function
funct1('she is','beautiful')  
funct1('and kind','hearted')

#fuction for calculator
def calci(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)
for i in range(2):
    n1=int(input('Enter a number'))
    n2=int(input('Enter the number'))
    calci(n1,n2)
