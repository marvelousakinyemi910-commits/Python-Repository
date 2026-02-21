number = int(input("Enter number: "))
number_string = str(number)
count = 0
for digit in number_string:
    count += 1
print(f"The number of digits is {count}")
