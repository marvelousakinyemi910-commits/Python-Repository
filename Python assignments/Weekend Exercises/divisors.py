number = int(input("Enter a number: "))
for count in range (1,number+1):
    if number % count == 0:
        print(count)
