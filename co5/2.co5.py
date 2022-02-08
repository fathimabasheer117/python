file=open("file1.txt",'r+')
list=[]
condition=True
while condition:
    x=file.readline()
    list.append(x)
    if not x:
        print("file ended")
        condition=False
fileobj=open("file2.txt",'a')
for i in range(0,len(list),2):
    fileobj.write(list[i])
fileobj.close()
file.close()
