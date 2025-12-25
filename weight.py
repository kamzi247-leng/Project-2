weight= float(input("Enter weight: "))
unit= input("Enter unit(kg/lb): ")

if unit == "kg":
    weight = weight * 2.20462
    print(f"Weight in pounds is {weight}lb.")
elif unit == "lb":
    weight = weight / 2.20462
    print(f"Weight in kilograms is {weight}kg.")
else:
    print("Invalid unit entered.")

print("End of program")