word = input("Enter word: ")
count = 0
for ch in word:
    if ch.islower():
        count += 1
print(f"The number of lower Case letters is {count}")
