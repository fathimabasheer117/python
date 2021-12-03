s=input("enter the string:")
b=s[0]
s=s[1:]
snew=s.replace(b,'$')
snew=b+snew
print(snew)
