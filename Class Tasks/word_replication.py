def word_replication(word,number):
    result = " "
    for index in range (len(word)):
        result += word[index] * number
    return result



                                                                                                                         








word = input("Enter a word: ")
number = int(input("Enter a number: "))
print(word_replication(word,number))
