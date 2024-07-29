n=int(input("enter an integer: "))
sum=0
for i in range(1,n):
 if(n%i==0):
     sum=sum+i
if(sum==n):
 print("it is perfect number")
else:
    print("it is not perfect number:")
