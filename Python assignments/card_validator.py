
def card_type(card_number):
    if card_number.startswith("4"):
       return "Visa Card"
    elif card_number.startswith("5"):
        return "MasterCard"
    elif card_number.startswith("37"):
        return "American Express Card"
    elif card_number.startswith("6"):
        return "Discover Card"
    else:
        return "Invalid Card"


def card_number(card_number):
    return card_number

def card_digit_length(card_number):
    length = len(card_number)

    
    if length >= 13 and length <= 16:
        return length
    else:
        return"Invalid card"    



def card_validity_status(card_number):
    card_number = card_number
    sum_even = 0
    sum_odd = 0
    reversed_card = card_number[::-1]

    for index, digit in enumerate(reversed_card)
        int 

        
        if index % 2 == 0:
            value = value* 2





























card_number = input('Hello, Kindly Enter Card details to verify: ')
print("Credit Card Type: ",card_type(card_number))
print("Credit Card Number: ",card_number)
print("Credit Card Digit Length: ",card_digit_length(card_number))

