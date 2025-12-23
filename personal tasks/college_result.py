
passes = 0
failures = 0

for student in range (10):
    result = int(input('Enter your result: (1 = pass, 2 = fail):' ))
    if result == 1:
        passes += 1
    else:
        failures += 1 
print ("passed: ", passes)
print("failured:",failures)
  
if passes > 8:
     print('Bonus to instructor')

