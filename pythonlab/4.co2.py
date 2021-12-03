u=int(input("enter the upper limit="))
l=int(input("enter the lower limit="))
li=[]
lst=[]
for x in range(1, u+1):
  if x%2==0:
      li.append(x)
for y in li:
    for z in range(1,y):
         if (z*z)==y:
             lst.append(y)
print(lst)
