#pseudocode
#Prompt a user to enter a number
#a prime number is a number divisible by one and itself,i.e it has two factors
#if it has divisors other then itself and 1 then it is not a prime number
#using a  loop to check each number 
#use another loop to the prime numbers before the given number
#display all the prime numbers between 1 and the given number

def prime_number ():
    number = int(input("Enter a number: "))
    print(f"The prime numbers between 1 and {number} are: ")
    for num in range(1,number + 1):
        if num <= 1:
            continue
        for factor in range(2,num):
            if num % factor == 0:
                break
        else:
            print(num)
prime_number ()
