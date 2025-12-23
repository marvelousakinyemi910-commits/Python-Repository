def card(card_number):

    if (card_number.isdigit()):
        return card_number
    else:
        raise TypeError("Card digits has non-numeric value ")


def card_digit_length(card_number):
    length = len(card(card_number))

    
    if length >= 13 and length <= 16:
        return length
       



def card_validity_status(card_number):
    sum_even = 0
    sum_odd = 0
    
    
    
    for index in range(1,card_digit_length(card_number)+1):
        value = card(card_number)[card_digit_length(card_number)-index]  
        value = int(value) 

        
        if (index % 2 == 0):
            value = value*2
            if(value>9):
                sum_even+= (value-9)
            else:
                sum_even+= value
        else:
            sum_odd += value
    total = sum_even+ sum_odd
    if(total%10 == 0):
        return"Valid"
    else:
        return"Invalid"



def card_type(card_number):
    if (card(card_number).startswith("4")):
        return(" Visa Card")
    elif(card(card_number).startswith("5")):
        return("MasterCard")
    elif (card(card_number).startswith("37")):
        return("American Express Card")
    elif(card(card_number).startswith("6")):
        return("Discover Card")
    else:
        raise TypeError("Card Type is not valid")
   




























card_number = input('Hello, Kindly Enter Card details to verify: ')
print("Credit Card Type: ",card_type(card_number))
print("Credit Card Number: ",card(card_number))
print("Credit Card Digit Length: ",card_digit_length(card_number))
print("Credit Card Validity status: ",card_validity_status(card_number))

