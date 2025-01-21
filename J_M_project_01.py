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
    print("Which of the two institutions is more fun, please?")
    better_institution = input()
    print("I understand. High school tends to be easier, but you'll do good in college, too!".format(better_institution))
    print("This class is part of the major called Information Technology. Please tell me why you picked this major.")
    reason_for_major = input()
    print("Good reason.".format(reason_for_major))
    print("Do you like coding?")
    yes_no_coding = input()
    print("Perfect! Let's start learning some Python today.".format(yes_no_coding))


    print("All responses")
    print(answer)
    print(college_name)
    print(high_school_name)
    print(better_institution)
    print(reason_for_major)
    print(yes_no_coding)

if __name__ == "__main__":
    main()
