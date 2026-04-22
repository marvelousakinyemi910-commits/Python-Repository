numbers = [23,56,54,89,90,80,25,32]

def perfect_square(number):
   square_root = int(number** 0.5)
   if square_root * square_root == number:
      return True
   return False

#print(perfect_square(16))
    


def check_if_sum_of_each_digits_is_a_perfect_square(numbers):
   
    digits = []
    for num in numbers:
        total = 0
        temp = num
        while temp > 0:
            total += temp % 10
            temp //= 10
        if perfect_square(total):
            digits.append(num)
    return digits

    

print(check_if_sum_of_each_digits_is_a_perfect_square(numbers))

def prime_number(number):
   
        if number <= 1:
            return False
        for factor in range(2,number):
            if number % factor == 0:
                return False
          
 
        return True
#print(prime_number(14))


def check_if_sum_of_each_digits_is_a_prime_number(numbers):
    digits = []
    for num in numbers:
        total = 0
        temp = num
        while temp > 0:
            total += temp % 10
            temp //= 10
        if prime_number(total):
            digits.append(num)
    return digits
print(check_if_sum_of_each_digits_is_a_prime_number(numbers))
    
