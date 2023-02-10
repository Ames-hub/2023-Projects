weight = input("Please enter your weight using your\npreferred unit of measurement: ")
weight.lower()
if "kg" in weight:
    weight = weight.replace("kg", "")
    weight = float(weight)
    print(f"Your weight is {weight * 2.205} pounds")
elif "lb" in weight:
    weight = weight.replace("lb", "")
    weight = float(weight)
    print(f"Your weight is {weight / 2.205} kilograms")