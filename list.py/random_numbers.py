import random
def random_numbers():
    numbers = []
    for index in range(10):
        number = random.randint(1,50)
        numbers.append(number)


    return numbers

def list_length(values):
    
    count = 0
    for value in values:
        count += 1
    return count

def sum_even_positions(numbers):
    
    total_even_positions = 0
    for index in range(len(numbers)):
        if index % 2 == 0:
            total_even_positions += numbers[index]
    return total_even_positions

def sum_odd_positions(numbers):
  
    total_odd_positions = 0
    for index in range(len(numbers)):
        if index % 2 != 0:
            total_odd_positions += numbers[index]
    return total_odd_positions

def multiply_third_position(numbers):
   
    multiply_third_positions = 1
    for index in range(len(numbers)):
        if index % 3 == 0:
            multiply_third_positions *= numbers[index] 
    return  multiply_third_positions
    
def average(numbers):
    
    total = 0
    for number in numbers:
        total += number
        average = total / len(numbers)
    return average

def largest_element(numbers):
   
   
    largest = numbers[0]
    for number in numbers:
        if number  > largest:
           largest  = number
    return largest

def smallest_element(numbers):
    
    smallest = numbers[0]
    for number in numbers:
        if number  < smallest:
           smallest  = number
    return smallest

def display_list_of_integer(numbers):
    
    for number in numbers:
        return number

def add_third_element(numbers):
   
    add_third_positions = 0
    for index in range(len(numbers)):
        if index % 3 == 0:
            add_third_positions += numbers[index] 
    return add_third_positions








    
    

        
        
    
    
