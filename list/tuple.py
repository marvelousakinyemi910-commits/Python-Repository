def length_of_tuple(numbers):
    count = 0
    for number in numbers:
        count += 1
    return count

numbers = (89,65,43,25)
print(length_of_tuple(numbers))

def reverse_string(word):
    reverse = ""
    for letter in word:
        reverse =  letter + reverse
    return reverse
word = ('r','a','c')
print(reverse_string(word))
    
