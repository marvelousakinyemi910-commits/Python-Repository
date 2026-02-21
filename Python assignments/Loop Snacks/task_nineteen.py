number = int(input("Enter numbers: "))
number_string = str(number)
largest = 0
for digit in number_string:
    digit_int= int(digit)
    if digit_int > largest:
        largest =  digit_int   
    
print(f"The largest is  {largest}")
