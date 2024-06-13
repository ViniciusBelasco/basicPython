# Create a program that reads an input phrase an shows:
#     How many times the letter 'A' appears.
#     The position where it appears for the first time
#     The position where  it appears for the last time

phrase = str(input("Enter a phrase: ")).upper().strip()

if phrase.count("A") == 0:
    print("No A letter was found sorry")
else:
    print(
        "The letter A appears {} times.\n"
        "The position it appears first is {}\n"
        "The last position it appears is {}".format(
            phrase.count("A"), phrase.find("A"), phrase.rfind("A")
        )
    )
