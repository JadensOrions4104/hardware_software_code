# I used Microsoft AI for this project after using the search: binary to decimal decimal to binary menu choose conversion check invalid try again python
# None of the teachings from you seemed to work for me unless I was quite lazy but it was due February 20th and I wanted a working program, okay Professor Nedd?

def greeting():
    print("This program converts binary numbers to decimal, and vice versa.")

def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

def decimal_to_binary(decimal_str):
    try:
        decimal = int(decimal_str)
        return bin(decimal)[2:]
    except ValueError:
        return None

def main():
    greeting()
    while True:
        print("\nConversion Menu:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            decimal = binary_to_decimal(binary_str)
            if decimal is not None:
                print(f"The decimal equivalent of {binary_str} is {decimal}.")
            else:
                print("Invalid binary number. Please try again.")
                while decimal is None:
                     binary_str = input("Enter a binary number: ")
                     decimal = binary_to_decimal(binary_str)
                     if decimal is not None:
                         print(f"The decimal equivalent of {binary_str} is {decimal}.")
                     else:
                         print("Invalid binary number. Please try again.")

        elif choice == '2':
            decimal_str = input("Enter a decimal number: ")
            binary = decimal_to_binary(decimal_str)
            if binary is not None:
                print(f"The binary equivalent of {decimal_str} is {binary}.")
            else:
                print("Invalid decimal number. Please try again.")
                while binary is None:
                     decimal_str = input("Enter a decimal number: ")
                     binary = decimal_to_binary(decimal_str)
                     if binary is not None:
                         print(f"The binary equivalent of {decimal_str} is {binary}.")
                     else:
                         print("Invalid decimal number. Please try again.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
