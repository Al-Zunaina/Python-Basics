import random
for i in range(5):
    var=random.randint(-20,78)
    var2=random.randint(-20,78)
    var3=random.randint(-20,78)
    var4=random.randint(-20,78)
    result=var*var3+var2-var4
    print(f'{var}*{var3}+{var2}-{var4}')
    ans=int(input('Enter the answer'))
    if ans==result:
        print('The answer is correct')
    else:
        print('The answer is incorrect')