word = input("Enter word: ")
count = 0
for character in word:
    if character.islower():
        count += 1
print(f"The number of lower Case letters is {count}")
