def addition():
    print("This program adds two numbers.")

def main():
    stop_loop = "no"
    addition()
    while stop_loop != "yes":
        num1 = input("Enter first number:")
        print("Okay. We'll take {}".format(num1))
        num2 = input("Enter second number:")
        print("Awesome! Let's take {} with the first number and add the two together!".format(num2))
        total = int(num1) + int(num2)
        print("{} + {} = {}".format(num1, num2, total))
        stop_loop = input("Type 'yes' to exit program: ").lower().strip()

if __name__ == "__main__":
    main()
