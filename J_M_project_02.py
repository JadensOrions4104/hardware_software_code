def conversation():
    print("Hello. I am going to ask you a series of questions so I can get to know a little more about you, if you don't mind. You can always end the conversation anytime by typing 'exit'.")
    print("What is your name, please?")
    answer = input()
    print("Great! Your name is {}.".format(answer))
    print("What's your favorite hobby, please?")
    fav_hobby = input()
    print("Great! Your favorite hobby is {}.".format(fav_hobby))
    print("What's your zodiac sign, please?")
    zodiac_sign = input()
    print("{} sounds awesome!".format(zodiac_sign))
    print("What's your lucky number, please?")
    lucky_number = input()
    print("Wow! That is lucky!".format(lucky_number))
    print("What's your favorite animal, please?")
    fav_animal = input()
    print("I love that!".format(fav_animal))
    print("Do you have any special talents, yes or no, please?")
    yes_no_talents = input().lower().strip()
    if yes_no_talents == "yes":
        print("What are they, please?")
        answer = input()
        print ("Wow, I would love to see that in-person!")
    elif answer == "no":
        print("Awwww, that's okay.")
    else:
        print("I can't make sense of this, sorry.")

def main():
    stop_loop = "no"
    conversation()
    while stop_loop != "yes":
        conversation_answer = conversation()
        print("Okay.". format(answer, conversation_answer) )
        stop_loop = input("Type 'yes' to exit program: ").lower().strip()
    print("All responses")
    print(answer)
    print(fav_hobby)
    print(zodiac_sign)
    print(lucky_number)
    print(fav_animal)
    print(yes_no_talents)

if __name__ == "__main__":
    main()
