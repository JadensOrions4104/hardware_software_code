def main():
    name = "Professor Nedd"
    print("Python is a type of coding program, and it might be the easiest one of all.")
    print("What is your name, please?")
    answer = input()
    print("Great! Your name is {}.".format(answer))
    print("What is the name of the college you are currently attending, please?")
    college_name = input()
    print("Great! You are currently attending {}.".format(college_name))
    print("What is the name of the high school you have attended, please?")
    high_school_name = input()
    print("{} is a great high school!".format(high_school_name))


    print("All responses")
    print(answer)
    print(college_name)
    print(high_school_name)


if __name__ == "__main__":
    main()
