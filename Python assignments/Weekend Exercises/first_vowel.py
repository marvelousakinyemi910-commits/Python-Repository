word = input("Enter word: ")
for letter in range(len(word)):
    if word[letter].lower() in "aeiou":
        print(f"Position of the first vowel is {letter}")
        break
