# Python
print("Adult body mass index Calculator")
weight=float(input("Enter the weight in KG= "))
height=float(input("Enter your height in meter= "))
Bmi=(weight/height)/height
print("Bmi=",Bmi)
if(Bmi<=18):
    print("Underweight")
elif(Bmi>18 and Bmi<=24):
    print("Weight is ohk")
else:
    print("Owerweight")
