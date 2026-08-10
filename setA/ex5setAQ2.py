def check(a):
    if a%2==0:
        return True
    else:
        return False
    
a=int(input("enter value  OF Number"))
if(check(a)==True):
    print("the number is true")
else:
    print("the number is false")