
def add_two_dictionaries(dictionary_one,dictionary_two):
    dictionary_one.update(dictionary_two)
  
    return dictionary_one


#def list_length(words):
#    count = 0
#    for word in words:
#        count += 1
#    return count
#
def length_of_list_as_key(words):
  
    dictionary_word = {}
#    for index, word in enumerate(words):
#         dictionary_word[index] = word
#    return dictionary_word

def total_and_average(student_grades):
    for name, grades in grades_book.items():
         total = sum(grades)
         average = total/ len(grades)

    
    

