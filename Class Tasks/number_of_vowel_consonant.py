
word = input('Enter a word: ')

sum_vowel = 0
sum_consonant = 0
for letter in word: 
    if(letter== "a" or letter== "e" or letter=="i" or letter=="o" or letter== "u"):
        sum_vowel += 1
       
    else:
        sum_consonant += ';'1
        
print("The sum of vowel is",sum_vowel,"\n")
print ("The sum of consonant is",sum_consonant)
