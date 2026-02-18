passes = 0
failures = 0
for student in range (15):
    score = int(input('Enter your scores: ' ))
    if score >= 45:
        passes += 1
    else:
        failures += 1 
print ("passed: ", passes)
print("failured:",failures)
  
