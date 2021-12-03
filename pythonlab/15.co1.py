lst1=[]
lst2=[]
print("enter the colors in list1:")
for x in range(1,5):
    a=str(input())
    lst1.append(a)
print("enter the colors in list2:")
for x in range(1,5):
    a=str(input())
    lst2.append(a)
print("list1:",lst1)
print("list2:",lst2)
s1=set(lst1)
s2=set(lst2)
print("the difference is :",s1.difference(s2))
