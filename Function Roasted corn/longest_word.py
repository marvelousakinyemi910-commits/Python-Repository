def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word)> len(longest):      
            longest = word
    return longest,len(longest)       
     

words = input("Enter a list of word separated by a comma: ").split()


print(longest_word(words)
