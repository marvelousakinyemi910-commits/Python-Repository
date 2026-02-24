word = input("Enter word: ")
count = 0
for character in word:
    if character.isupper():
        count += 1
print(f"The number of Upper Case letters is {count}")
