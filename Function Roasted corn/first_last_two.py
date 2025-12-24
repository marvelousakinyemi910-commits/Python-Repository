def first_last_two(word):
    if len(word ) < 2:
        return ""
    return word[:2]+ word[-2:]

word = input("Enter a word: ")
print(first_last_two(word))
