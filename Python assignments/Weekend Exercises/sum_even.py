number = int(input("Enter a number: "))
counter = 0
for count in range (1,number+1):
    if number % 2 == 0:
        counter += 1
print(f"The number of even number is {counter}")
