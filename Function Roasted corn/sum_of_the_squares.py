def sum_0f_the_squares(numbers):
    total = 0
  
    for num in numbers:
        total+= num**2
    return total




numbers = input('Enter a list of numbers separated by a space: ').split()

numbers = [int (num)for num in numbers ]


print(sum_0f_the_squares(numbers))
