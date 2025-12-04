speed = float(input("Enter speed:"))
acceleration = float(input("Enter acceleration:"))

minimum_runway_length = (speed*speed)/ (2*acceleration)

print("The minimum runaway length of the airplane: ",round(minimum_runway_length,2))
