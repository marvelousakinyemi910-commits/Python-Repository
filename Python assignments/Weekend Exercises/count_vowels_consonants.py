word = input("Enter word: ")
count_vowel = 0
count_consonant = 0
for letter in range(len(word)):
    if word[letter].lower() in "aeiou":
        count_vowel += 1
       
    else:
        count_consonant += 1
          
print(f"The number of vowels in the word are : {count_vowel}")       
print(f"The number of consonants in the word are : {count_consonant}")  
