number = int(input('Enter a number: ' ))

for num in range(number,0,-1):
    for length in range(num, 0,-1):     
        print(length,end= ' ')
    print()
