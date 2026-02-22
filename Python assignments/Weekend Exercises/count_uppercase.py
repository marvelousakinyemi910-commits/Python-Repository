word = input("Enter word: ")
count = 0
for ch in word:
    if ch.isupper():
        count += 1
print(f"The number of Upper Case letters is {count}")
