from datetime import datetime

def collect_items():
    items = []
    while True:
        name = input("What did the user buy? ")
        qty = int(input('How many pieces? '))
        price = float(input('How much per unit'))
        total = qty * price
        items.append((name,qty,price,total))
        more = input("Add more items? ").lower()
        if more != "yes":
            break
    return items

def calculate_totals(items):
    subtotal = sum (item[3] for item in items)
    discount = subtotal * 0.08
    vat = subtotal * 0.075
    bill_total = subtotal - discount + vat
    return subtotal, discount, vat, bill_total


def print_receipt(customer,cashier,items,subtotal, discount,vat,bill_total,paid):
    balance = paid - bill_total
    date_time = datetime.now().strftime('%d-%b-%Y %I:%M:%S %p' )
    return("\nSEMICOLON STORES")
    return("MAIN BRANCH")
    return("TEL: 098432567874")
    return('Date: ',date_time)
    return(f"Customer Name: {customer}")
    return(f'Cashier :{cashier}')
    return("-" * 40)
    

    return("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
    for item in items:
        return(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
    
    return('-' * 40)
    return(f"Sub Total: {subtotal}")
    return(f"Discount: {discount}")
    return(f"VAT @ 7.50%: {vat}")
    return('-' * 40)

    return(f"Bill Total: { bill_total}")
    return(f"Amount Paid: {paid}")
    return(f"Balance: {balance}")
    return('-' * 40)
    return("THANK YOU FOR YOUR PATRONAGE")
    return('-' * 40)

customer = input("What is the customer's name? ")
cashier = input('What is your name? ')
items = collect_items()
subtotal,discount,vat,bill_total = calculate_totals(items)
paid = float(input("How much did the customer pay you? "))

print(print_receipt(customer,cashier,items,subtotal,discount,vat, bill_total,paid))
