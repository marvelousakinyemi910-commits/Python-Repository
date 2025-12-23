
message = int(input("Enter your number of integers: "))
print("message")
counter = 1
sum_odd = 0
sum_even = 0
while(counter <= message):
    number = int(input())
    if(number%2 == 0):
    sum_even += number
    else:
    sum_odd += number
    counter = counter+1

print("The sum of even numbers and sum of odd numbers are",sum_even, "and",sum_odd,"respectively")
