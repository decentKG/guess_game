def show_intro():
    print("Welcome to the AC vs DC Explainer")
    print("Ths App will help you to understand the differrence between " \
    "Alternative Current and Direct Current")

def show_ac_info():
    print("\n Alternative Current(AC)")
    print("Electricity flos back and forth")
    print("Used in homes and buildings. ")
    print("Can travel long distance easily")
    print("Invented by Nikola Tela.\n")

def show_dc_info():
    print("\n Direct Current (DC):")
    print("Electricity flows in one direction")
    print("Used in Batteries, Phones and EVs")
    print("Better for short distance")
    print("Promoted by Thomas Edison, \n")

def show_difference():
    print("\n Key Difference: ")
    print("AC: Reverses direction | DC: Constant direction")
    print("AC: Used in power grids | DC: Used in electronics")
    print("AC: Can be transformed in voltage easily | DC: Can not (needs convertrer)\n")

def menu():
    while True:
        print("MENU")
        print("1. Learn about AC")
        print("2. Learn about DC")
        print("3. Compare AC nad DC")
        print("4. Exit\n")
        choice = input("ENTER YOUR CHOICE(1-4): ")

        if choice == '1':
            show_ac_info()
        elif choice == '2':
            show_dc_info()
        elif choice == '3':
            show_difference()
        elif choice == '4':
            print("Thanks for learning with US,,See yo next time")
            
            break
        else:
            print("Invalid input, try again. \n")

show_intro()
menu()


