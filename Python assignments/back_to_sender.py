menu = """
_____________________________________________
|Collection Rate| Amount Per Parcel |Base Pay|
|_______________|___________________|________|
|Less than 50%  | 160               |5,000   |
|_______________|___________________|________|
|50 - 59%       | 200               |5,000   |
|_______________|___________________|________|
|60 - 69%       | 250               |5,000   |
|_______________|___________________|________|
|>=70%          | 500               |5,000   |
|_______________|___________________|________|

"""
print(menu)




def riders_wage(no_successful_delivery):
    no_successful_delivery = no_successful_delivery
    if no_successful_delivery < 0 or no_successful_delivery > 100:
        return("Invalid number of successful delivery! Kindly enter a valid number")
    elif no_successful_delivery >= 70:
        amount_per_parcel = 500
        base_pay = 5000
    elif 70 < no_successful_delivery >60:
        amount_per_parcel = 250
        base_pay = 5000
    elif 60 < no_successful_delivery > 50:
        amount_per_parcel = 200
        base_pay = 5000
    elif no_successful_delivery < 50:
        amount_per_parcel = 160
        base_pay = 5000
    else:
        return"Invalid number of delivery"
    wage = no_successful_delivery * amount_per_parcel + base_pay
    return (f"The rider's wage is: {wage}")
    
no_successful_delivery = int(input("Enter number of successful delivery: "))
print(riders_wage(no_successful_delivery))
