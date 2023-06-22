from dictionaries import dictionaries
import colors

sections = list(dictionaries.keys())

# Create a dictionary to store user responses
user_data = {}

# Ask the first set of questions
age = input(colors.CYAN + colors.BOLD + "1. Leeftijd: " + colors.RESET)
gender = input(colors.CYAN + colors.BOLD + "2. Geslacht (man/vrouw/anders): " + colors.RESET)
education = input(colors.CYAN + colors.BOLD + "3. Opleidingsniveau: " + colors.RESET)

# Save the answers in user_data
user_data["Leeftijd"] = age
user_data["Geslacht"] = gender
user_data["Opleidingsniveau"] = education

# Iterate over the sections and ask the remaining questions
for section in sections:
    questions = dictionaries[section]
    question_keys = list(questions.keys())
    main_question = questions[question_keys[0]]

    valid_answers = ["nee", "ja"]

    while True:
        answer = input(colors.CYAN + colors.BOLD + "1. " + main_question +
                       colors.RESET + colors.BLUE + " (ja/nee): " + colors.RESET).lower()

        if answer in valid_answers:
            break
        else:
            print(colors.RED + "Ongeldig antwoord." + colors.BLUE +
                  " Vul a.u.b. 'ja' of 'nee' in." + colors.RESET)

    # Save the answer in user_data
    user_data[main_question] = answer

    if answer == "nee":
        for i in range(1, 5):
            question = questions[question_keys[i]]
            print(colors.YELLOW + colors.BOLD +
                  str(i + 1) + ". " + question + colors.RESET)
            while True:
                sub_answer = input("> ").lower()
                if sub_answer in valid_answers:
                    break
                else:
                    print(colors.RED + "Ongeldig antwoord." + colors.BLUE +
                          " Vul a.u.b. 'ja' of 'nee' in." + colors.RESET)
            # Save the sub-answer in user_data
            user_data[question] = sub_answer
        print()
    elif answer == "ja":
        print(colors.MAGENTA + colors.BOLD +
              " \n Dit is de reden dat je last hebt van prestatie motivatie!  \n" + colors.RESET)

        # Save the final answer in user_data
        user_data["Reden prestatie motivatie"] = answer

        break

# Ask the final question
print()
print(colors.CYAN + colors.BOLD + "Will je deze uitkomst uitgeprint hebben? (ja/nee): " + colors.RESET)
print()
print_answer = input(colors.BLUE + "> " + colors.RESET).lower()

# Save the answer in user_data
user_data["Uitkomst uitgeprint"] = print_answer

# Ask the user for a name for the data file
file_name = input(
    "Geef de naam van het tekstbestand waarin u de gegevens wilt opslaan: ")

# Save the user data to the specified file
with open(file_name + ".txt", "w") as file:
    for key, value in user_data.items():
        file.write(key + ": " + value + "\n")

print("De gegevens zijn opgeslagen in het bestand:", file_name)
