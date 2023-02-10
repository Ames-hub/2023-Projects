print("Height converter")
height = input("Please enter your height using your\npreferred unit of measurement: ")

height.lower()
if "cm" in height:
    height = height.replace("cm", "")
    height = float(height)
    print(f"Your height is {height // 2.54} inches")

elif "in" in height:
    height = height.replace("in", "")
    height = float(height)
    height = height * 2.54
    print(f"Your height is {height * 2.54} centimeters")