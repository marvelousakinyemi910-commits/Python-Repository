from functools import reduce
fruits = ["apple", "banana","kiwi","grapes","cherry" ]
numbers = [1,2,3,4,5]
words = ["1","Love","python","snacks"]


def get_square(number):
    square = number * number
    return square
square = list(map(get_square, numbers))
print(square)

def get_length(word):
    length = len(word)
    return length
length = list(map(get_length,fruits))
print(length)



def is_even(number):
    return number % 2 == 0
filtered_numbers = list(filter(is_even,numbers))
print(filtered_numbers)
    

def has_longer_letters(words):
    return len(words) > 5
filtered_words = list(filter(has_longer_letters,words))

print(filtered_words)


def concatenate_string(accumulator,element):
    return accumulator +"-" + element
print(reduce(concatenate_string,words))



