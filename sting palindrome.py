def isPalindrome(s):
    return s == s[::-1]

s=input("enter string:")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")