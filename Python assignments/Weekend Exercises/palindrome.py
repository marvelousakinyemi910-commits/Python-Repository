word = input("Enter a word: ")
reversed_word = ""
for count in range(len(word)-1, -1,-1):
    reversed_word+= word[count]
if reversed_word== word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
