x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
elif y == 0:
    print("X-axis")
elif x > 0 and y > 0 :
    print("Q1")
elif x < 0 and y > 0 :
    print("Q2")
elif x < 0 and y < 0 :
    print ("Q3")
else:
    print("Q4")
