def show_menu():
    print("======== UNIT CONVERTER =========")
    print("1. Lenght Converter")
    print("2.  Temperature Converter")
    print("3. Exit")

show_menu()    

choice = input("Enter Your choice(1-3):").strip()

if choice == "1":
    print("======= Length Converter =======")
    print("Kilometers to Meters")
    print("Meters to Centimeters")
    print("Centimeters to Miles")

    length_choice = input("Enter Your choice(1-3):")

    if length_choice == "1":
        km = float(input("Enter KiloMeters:"))
        meters = km * 1000
        print("Meters:", meters)

    elif length_choice == "2":
        meters = float(input("Enter Meter:"))
        centimeters = meters * 100 
        print("CentiMeters:", centimeters)

    elif length_choice == "3":
        km = float(input("Enter KiloMeters:"))
        miles = km * 0.621371
        print("Miles:", miles)    

elif choice == "2":
    print("======Temperature Converter=======")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

elif choice == "3":
    print("Unit Converter Closed")   

else:
    print("Invalid Choice!")         

