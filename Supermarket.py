dict1={}
while True:
    user_input=input("Enter item with Price=")
    if not user_input:
        break
    temp=user_input.split()
    price=temp[-1]
    item=" ".join(temp[:-1])
    dict1[item]=dict1.get(item,0)+int(price)
for k,v in dict1.items():
    print(k,v)
