#factorial program
#1 RECCURSIVE
def f(n):
    if n==0:
        return 1
    return n*f(n-1)
# 2ITERATIVE
def f(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res
n=4
print(f(n))