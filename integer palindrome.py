#integer palindrome
def isPalindrome(self, x: int) -> bool:
        z=str(x)
        y=z[::-1]
        if z==y:
            return True
        else:
            return False
        
def ispalindrome(x):
    if x<0 or x>0 and x%10==0:
          return False
    res=0
    while x>res:
          res=res*10+x%10
          x=x//10
    return x==res or x==res//10 