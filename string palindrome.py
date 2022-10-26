#string palindrome
def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalnum():
                a+=i
        b=a.lower()
        return b==b[::-1]
s=input()
print(isPalindrome(s))