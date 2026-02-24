number = int(input("Enter a number: "))
counter = 0
for count in range (1,number+1):
    if number % 2 == 1:
        counter += 1
print(f"The number of odd numbers are {counter}")
