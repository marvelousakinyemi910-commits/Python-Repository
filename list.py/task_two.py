from functools import reduce

values = ["1","2","3"]
numbers = [1,5,10,15]
collection = [1,None,3,None,5]
integers = [-2,-1,0,1,2]
words = ["Hello", " ", "World"]

def convert_to_integer(value):
    integer = int(value)
    return integer
integer = list(map(convert_to_integer,values))
print(integer)   


def add_ten_to_each_element(value):
    add_ten = value + 10
    return add_ten
add_ten = list(map(add_ten_to_each_element,numbers))
print(add_ten)


def convert_to_fahrenheit(number):
    fahrenheit =  number * 1.8 + 32
    return fahrenheit
fahrenheit = list(map(convert_to_fahrenheit,numbers))
print(fahrenheit)



def is_number(value):
    return value != None
filtered_values = list(filter(is_number,collection))
print(filtered_values)


def is_divisible_by_3(value):
    return value % 3 == 0
filtered_values = list(filter(is_divisible_by_3,numbers))
print(filtered_values)


def is_positive_number(value):
    return value > 0
filtered_values = list(filter(is_positive_number,integers))
print(filtered_values)    


def product_of_numbers(accumulator,element):
    return accumulator * element
print(reduce(product_of_numbers,numbers))

def maximum_value(maximum,element):
    if maximum > element:
        return maximum
    else:
        return element
print(reduce(maximum_value,numbers))

def concatenate_string(accumulator,element):
    return accumulator + element
print(reduce(concatenate_string,words))

