
counter = 1
sum_odd = 0
sum_even = 0
while(counter <= 20):
    print("Enter a number")
    number = int(input())
    if(number%2 == 0):
        sum_even += number
    else:
        sum_odd += number
    counter = counter+1

print("The sum of even is",sum_even,"\n")
print ("The sum of odd is",sum_odd)
