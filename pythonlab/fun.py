def armstrong(s):
 s=int(input("enter a number :"))
sum=0
temp=s


while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
    
if s==sum:
 print(s," is an Armstrong number")
else:
 print(s,"is not an Armstrong number")
armstrong(s)

