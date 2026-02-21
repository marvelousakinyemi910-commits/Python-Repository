number = int(input("Enter numbers: "))
number_string = str(number)
smallest = 9
for digit in number_string:
    digit_int= int(digit)
    if digit_int < smallest:
        smallest =  digit_int   
    
print(f"The smallest is  {smallest}")
