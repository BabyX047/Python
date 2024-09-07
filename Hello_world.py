print("\nHello, There!")

name = input("\nWhat is your name: ")

print("\nWelcome, " + name + "!\n")

coding = input("Want to learn coding? Y/N \n").lower()

if coding == 'n':
    print("\nHope you change your mind soon!")
    exit()

age = int(input("How old are you: \n"))

if coding == 'y' and 6 <= age <= 13:
    print("\nGreat choice! Coding is an important skill for many jobs.\n")
    print("We shall begin with Scratch")

    shall_we_begin = input("Shall we begin? Y/N \n").lower()

    if shall_we_begin == 'y':
        print("\nAwesome! Let's start learning Scratch!")
    else:
        print("\nNo worries! We can start whenever you're ready.")

elif 14 <= age <= 30:
    print("\nYou are at a great age to start learning coding! It's never too late.\n")
    print("Here are some popular coding languages:")
    print("\t- Python")
    print("\t- Java")
    print("\t- C++")
    print("\t- JavaScript")

    language = input("What language do we begin with? \n").capitalize()

    if language in ["Python", "Java", "C++", "Javascript"]:
        shall_we_begin = input(f"Great, shall we begin?  Y/N \n").lower()

        if shall_we_begin == 'y':
            print(f"\nAwesome! Let's start learning {language}!")
        else:
            print(f"\nNo worries! We can start {language} whenever you're ready.")
    else:
        print("\nSorry, that's not a valid language choice.")

else:
    print("\nI'm sorry, but your age does not meet the criteria for learning coding.\n")
