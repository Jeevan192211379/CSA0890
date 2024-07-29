temp=int(input("enter an integer: "))
rev=0

while (temp!=0):
    r=temp%10
    rev=rev+r
    temp=temp//10
print(rev)
