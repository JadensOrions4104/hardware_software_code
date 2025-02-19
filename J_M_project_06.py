def greeting():
    print(This program converts decimals to binary, vice versa.)

def display_menu():
    menu_dict = ’1’:’decimal to binary’, ’2’:’binary to decimal’
}
    print("Choose a number conversion")
    for items, values in menu_dict.items():
        print(“\t{}. {}".format(items,value))
    choice = input("{} ".format(choose)).upper().strip()
    choices = list(menu_dict.keys())
    if choice in choices:
        return menu_dict[choice]
    else:
        return(display_menu("Invalid Selection. Try Again."))

def check_decimal(decimal_str):
    valid_decimal = ['0','1','2','3','4','5','6','7','8','9']

    if decimal_str in valid_decimal:
        return decimal_str
    else:
        check_decimal(input("Invalid decimal, try again."))

def check_binary(binary_str):
    valid_binary = ['0','1']

    if binary_str in valid_binary:
        return binary_str
    else:
        check_binary(input("Invalid binary, try again."))

def main():
    greeting()
    display_menu()
    check_decimal()
    check_binary()

if __name__ == "__main__":
    main()
