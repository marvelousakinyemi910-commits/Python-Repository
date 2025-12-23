message = "Enter your number of integers: "
number_of_value = int(input(message))
counter = 1
sum_odd = 0
sum_even = 0
while(counter <= number_of_value):
    print("Enter a number")
    number = int(input( ))
    if(number%2 == 0):
        sum_even= number+sum_even
    else:
        sum_odd = number+sum_odd
    counter = counter+1

print("The sum of even numbers and sum of odd numbers are",sum_even, "and",sum_odd,"respectively")
