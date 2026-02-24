principal = int(input("Enter loan amount: "))
years = int(input("Enter the number of years: "))
duration = years * 12

print('Interest Rate  Monthly Payment Total Payment')
for interest_rate in range(500, 1001,25):
    interest = interest_rate / 100
    rate = interest / (100*12)
    monthly_payment = (principal * rate *(1 + rate)** duration) / ((1 + rate)** duration -1)
    total = monthly_payment * 12
    print(f"{interest:7.3f}% {monthly_payment:10.2f}{total:10.2f}")
