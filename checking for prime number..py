from math import sqrt


n=int(input())
def f(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
print(f(n))