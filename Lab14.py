def binary_to_decimal():
    global num
    num = input ("Enter Binary Number: ")
    result = 0
    if len(num) > 0:
        power = len(str(num)) - 1 # determine greatest power
        for num in str(num):
            result += int(num) * 2 ** power
            power -= 1 # decrease by 1
        return result

def main():
    stop_loop = "no"
    binary_to_decimal()
    while stop_loop != "yes":
        binary_num = binary_to_decimal()
        print("Binary {} to Decimal: {}". format(num, binary_num) )
        stop_loop = input("Type 'yes' to exit program: ").lower().strip()

if __name__ == "__main__":
    main()
