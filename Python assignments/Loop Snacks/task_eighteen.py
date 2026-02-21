number = int(input("Enter numbers: "))
number_string = str(number)
total = 0
for digit in number_string:
    total += int(digit)
    
print(f"The sum of digits is {total}")
