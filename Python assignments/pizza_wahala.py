def pizza_wahala(people,pizza_type):
    pizza_type = pizza_type.lower()
    if pizza_type == "sapa size":
        number_of_slices = 4
        price_per_box = 2000
    elif pizza_type == "small money":
        number_of_slices = 6
        price_per_box = 2400
    elif pizza_type == "big boys":
        number_of_slices = 8
        price_per_box = 3000
    elif pizza_type == "odogwu":
        number_of_slices = 12
        price_per_box = 4200
    else:
        return"Invalid pizza type"
    boxes = people // number_of_slices
    if people % number_of_slices != 0:
        boxes += 1
    total_slices = boxes * number_of_slices
    leftover_slices = total_slices - people
    total_cost = boxes * price_per_box

    return(
        f"Number of boxes of pizza to buy = {boxes}\n"
        f"Number of leftover slices after serving = {leftover_slices}\n"
        f"price = N{total_cost}"
        )
people = int(input("Enter number of guests: "))
pizza_type = input("What Pizza type do you want? ")

print(pizza_wahala(people,pizza_type))
