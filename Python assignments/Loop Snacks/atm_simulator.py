#initialise balance to be 1000
#initialise option to be 0
#using a loop display the options and 4 prompt the user to choose between deposit, withdraw or check balance option
#use selection statement in each option
# when deposit is made, add to the balance
#when withdrawal is made, subtract from the balance
#sentinel value should be option for exit
# use if statement to make sure withdrawal is not more than balance


def atm_simulator():
    balance = 1000
    option = 0
    while option != 4:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        option = int(input('Choose an option: '))
        if option == 1:
            amount = int(input(  'Enter amount to deposit'))
            balance += amount
            print("Deposit successful")
        elif option == 2:
            amount = int(input('Enter amount to withdraw: '))
            if amount > balance:
                print("Insufficient fund")      
            else:
                balance -= amount
                print("Withdrawal successful")
        elif option == 3:
            print(f"Balance is #{balance}")
        elif option == 4:
            print("Thank you for using our atm! ")
        else:
            print("Inavlid option")
        
       
atm_simulator()
