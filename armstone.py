c=input("Enter a no")
b=len(c)
a=int(c)
d=a
result=0
while (a>0):
    x=a%10
    result=result+x**int(b)
    a=a//10
print(result)
if (d==result):
    print("Armstrong no")
else:
    print("Not armstrong")
