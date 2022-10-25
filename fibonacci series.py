
def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
n=int(input())
print(f(n))


'''def f(n):
        a=0
        b=1
        if n<0:
            return 'negative'
        if n==0:
            return a
        if n==1:
             return b
        else:
             for i in range(2,n+1):
                  c=a+b
                  a=b
                  b=c
            return c
'''
