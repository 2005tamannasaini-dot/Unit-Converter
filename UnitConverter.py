def show_menu():
    print("======== UNIT CONVERTER =========")
    print("1. Lenght Converter")
    print("2.  Temperature Converter")
    print("3. Exit")

show_menu()    

choice = input("Enter Your choice(1-3):").strip()

if choice == "1":
    print("Lenght Converter Selected")

elif choice == "2":
    print("Temperature Converter Selected")

elif choice == "3":
    print("Unit Converter Closed")   

else:
    print("Invalid Choice!")         

