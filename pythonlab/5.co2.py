n=int(input("enter no. of steps:"))
for i in range(n):
    s= " "
    for j in range(i+1):
       s= s+" "+str((i+1)*(j+1))
    print(s)
