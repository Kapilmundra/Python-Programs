a=int(input("Enter a no"))
b=a
rev=0
while (a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
if (b==rev):
    print("Pallindrome")
else:
    print("Not Pallindrome")
