word = input('Enter a word that contains letter e: ')
count = 0
for letters in word:
    if letters == 'e':
        count += 1
print(f"The number of times e appered in {word} is {count} times")
