n=int(input("enter the no of rows:"))
for i in range(n,0,-1):
  for j in range(0,n-i):
      print(" ",end=" ")
  for j in range(0,i+1):
      print("* ",end=" ")
  print()
