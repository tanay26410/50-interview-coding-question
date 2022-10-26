#armstrong number
def arm(n):
    sum1=0
    a=n
    b=len(str(n))
    while n:
        sum1+=(n%10)**b
        n=n//10
    return sum1==a
n=153
print(arm(n))