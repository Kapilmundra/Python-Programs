
print("Ride Cost Calculator")
DisTravel=float(input("Enter the distance Travel in KM= "))
CostDiesel=float(input("Enter the Cost of Diesel= "))
FuelAvg=float(input("Enter the fuel avg= "))
CostofDrive=(DisTravel/FuelAvg)*CostDiesel
print("Cost of drive= ",CostofDrive)
