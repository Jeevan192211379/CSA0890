n=int(input("enter an integer: "))
sum=0
temp=n
while(temp!=0):
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if(n==sum):
    print("armstrong")
else:
    print("not armstrong")
