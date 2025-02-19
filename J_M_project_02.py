def closing_statement(count):
    if count == 0:
        print("Awww, that's okay. We can always chat another day.")
        print("0 questions have been answered.")
    else:
        print("Okay. It was nice to meet you!")
        print("{} questions have been answered.".format(count))

def conversation():
    count = 0
    while True:
        print("Hello. I am going to ask you a series of questions so I can get to know a little more about you, if you don't mind. You can always end the conversation anytime by typing 'exit'.")
        print("What is your name, please?")
        answer = input()
        if answer.lower() == " exit" or answer.lower() == "exit " or answer.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("Great! Your name is {}.".format(answer))
        print("What's your favorite hobby, please?")
        fav_hobby = input()
        if fav_hobby.lower() == " exit" or fav_hobby.lower() == "exit " or fav_hobby.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("Great! Your favorite hobby is {}.".format(fav_hobby))
        print("What's your zodiac sign, please?")
        zodiac_sign = input()
        if zodiac_sign.lower() == " exit" or zodiac_sign.lower() == "exit " or zodiac_sign.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("{} sounds awesome!".format(zodiac_sign))
        print("What's your lucky number, please?")
        lucky_number = input()
        if lucky_number.lower() == " exit" or lucky_number.lower() == "exit " or lucky_number.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("Wow! That is lucky!".format(lucky_number))
        print("What's your favorite animal, please?")
        fav_animal = input()
        if fav_animal.lower() == " exit" or fav_animal.lower() == "exit " or fav_animal.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("I love that!".format(fav_animal))
        print("What's your favorite color, please?")
        fav_color = input()
        if fav_color.lower() == " exit" or fav_color.lower() == "exit " or fav_color.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("Fantastic color!".format(fav_color))
        print("Where's your favorite place to go, please?")
        fav_place = input()
        if fav_place.lower() == " exit" or fav_place.lower() == "exit " or fav_place.lower() == "exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("What a lovely place!".format(fav_place))
        print("Do you have any special talents, yes or no, please?")
        yes_no_talents = input().lower().strip()
        if yes_no_talents.lower() == " exit" or yes_no_talents.lower() == "exit " or yes_no_talents.lower() == "exit":
            closing_statement(count)
            break
        elif yes_no_talents.lower() == "yes" or yes_no_talents.lower() == "yes " or yes_no_talents.lower() == " yes":
            print("What are they, please?")
            answer = input()
            count +=1
            print ("Wow, I would love to see that in-person!")
        elif yes_no_talents.lower() == "no" or yes_no_talents.lower() == "no " or yes_no_talents.lower() == " no":
            print("Awwww, that's okay.")
            count +=1
        else:
            print("I can't make sense of this, sorry.")

def main():
    conversation()
    # counter = 10
    # while_loop(counter)
    # for_loop(counter)
    # print("All responses")
    # print(answer)
    # print(fav_hobby)
    # print(zodiac_sign)
    # print(lucky_number)
    # print(fav_animal)
    # print(fav_color)
    # print(fav_place)
    # print(yes_no_talents)

if __name__ == "__main__":
    main()
