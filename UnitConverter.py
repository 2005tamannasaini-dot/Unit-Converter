## UNTI CONVERTER PROJECR

def km_to_meters(km):
    return km * 1000

def meters_to_cm(meters):
    return meters * 100

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def show_menu():
    print("======== UNIT CONVERTER =========")
    print("1. Length Converter")
    print("2. Temperature Converter")
    print("3. Exit")

show_menu()    

choice = input("Enter Your choice(1-3):").strip()

if choice == "1":
    print("======= Length Converter =======")
    print("1. Kilometers to Meters")
    print("2. Meters to Centimeters")
    print("3. Kilometers to Miles")

    length_choice = input("Enter Your choice(1-3):")

    if length_choice not in["1", "2", "3"]: 
        print("Invalid Length Choice!")

    else:
        if length_choice == "1":
            try:
                km = float(input("Enter KiloMeters:"))
                meters = km_to_meters(km)
                print("Meters:", meters)
            except ValueError:
                 print("Please enter a valid number!")

        elif length_choice == "2":
            try:
                meters = float(input("Enter Meter:"))
                cm = meters_to_cm(meters)
                print("CentiMeters:", cm)
            except ValueError:
                 print("Please enter a valid number!")

        elif length_choice == "3":
            try:
                km = float(input("Enter KiloMeters:"))
                miles = km_to_miles(km)
                print("Miles:", miles)    
            except ValueError:
                 print("Please enter a valid number!")    

elif choice == "2":
    print("======Temperature Converter=======")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    temp_choice = input("Enter Your Choice(1-2):")

    if temp_choice not in["1", "2",]: 
            print("Invalid Temperature Choice!")
    
    elif temp_choice == "1":
        try:
            celsius = float(input("Temperature in Celsius:" ))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Fahrenheit:", fahrenheit)
        except ValueError:
             print("Please enter a valid number!")

    elif temp_choice == "2":
        try:
            fahrenheit = float(input("Temperature in Fahrenheit:"))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Celsius:", celsius)
        except ValueError:
             print("Please enter a valid number!")    

elif choice == "3":
    print("Unit Converter Closed")   

else:
    print("Invalid Choice!")         


