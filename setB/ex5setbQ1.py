def check(num):
    if num<=1:
        return False
    for a in range(2,num):
        if(num%a==0):
            return False
        else:
            return True
        

a=int(input("enter value  OF Number"))
if(check(a)==True):
    print(f'number is prime')
else:
    print(f'numer is not prime')

        