numbers = {1,5,6,2,5,1,3,4}
print(len(numbers))


def is_prime_number(number):
   
    if number <= 1:
        return False
    for factor in range(2,number):
        if number % factor == 0:
            return False
          
 
    return True


def set_of_prime_numbers(numbers):
    prime_num = set()
    
    for num in numbers:
        if prime_number(num):
            prime_num.add(num)
        return prime_num
print(set_of_prime_numbers(numbers))
  
