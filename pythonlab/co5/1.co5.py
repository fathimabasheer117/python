file=open("file.txt","r")
list=[]
condition=True
while condition:
    x=file.readline()
    list.append(x)
    if not x:
        condition=False
print("the file converted into list:")
print(list)
