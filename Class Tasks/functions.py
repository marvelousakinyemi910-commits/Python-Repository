def sum_multiple():
    for numbers in range(20_001):
        total = 0

    if numbers % 10 == 0:
        total += numbers
    print(total)
sum_multiple()

def multiples_of_three():
    for number in range(0,45,3):
        print(number,end = ' ')
multiples_of_three()

def even_number():
    for number in range(0,100,2):
        print(number,end = ' ')
even_number()

def score_grade():
    passes = 0
    failures = 0
    for student in range (15):
        score = int(input('Enter your scores: ' ))
        if score >= 45:
            passes += 1
        else:
            failures += 1 
    print ("passed: ", passes)
    print("failured:",failures)
score_grade()
  
def multiplication():
    multiplier = int(input('Enter a multiplier: ' ))
        for number in range(1,11):
            result = f"{multiplier} X {number} = {multiplier *number}"   
            print(result) 
multiplication()

def Star_pattern():
    number = int(input('Enter a number: ' ))

    for num in range(number+1):
        for length in range(num):     
            print("*",end= ' ')
        print()

def number_pattern():
    number = int(input('Enter a number: ' ))

    for num in range(number,0,-1):
        for length in range(num, 0,-1):     
            print(length,end= ' ')
        print()
