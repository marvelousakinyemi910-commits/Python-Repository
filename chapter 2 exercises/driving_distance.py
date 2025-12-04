

distance = float(input("Enter driving distance: "))
miles_per_gallon = float(input("Enter miles per gallon: "))
price = float(input("Enter price per gallon: "))

cost_of_driving = (distance*price)/miles_per_gallon

print("cost of trip is $"+ str(cost_of_driving))
