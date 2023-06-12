from dictionaries import dictionaries
import colors

sections = list(dictionaries.keys())

# Iterate over the sections and ask the questions
for section in sections:
    questions = dictionaries[section]
    question_keys = list(questions.keys())
    main_question = questions[question_keys[0]]

    valid_answers = ["nee", "ja"]

    while True:
        answer = input(colors.CYAN + colors.BOLD + "1. " + main_question + colors.RESET + colors.BLUE +" (ja/nee): " + colors.RESET).lower()

        if answer in valid_answers:
            break
        else:
            print(colors.RED + "Ongeldig antwoord." + colors.BLUE + " Vul a.u.b. 'ja' of 'nee' in." + colors.RESET)

    if answer == "nee":
        for i in range(1, 5):
            question = questions[question_keys[i]]
            print(colors.YELLOW + colors.BOLD + str(i + 1) + ". " +  question + colors.RESET)
            while True:
                sub_answer = input("> ").lower()
                if sub_answer in valid_answers:
                    break
                else:
                    print(colors.RED + "Ongeldig antwoord." + colors.BLUE + " Vul a.u.b. 'ja' of 'nee' in." + colors.RESET)
        print()
    elif answer == "ja":
        print(colors.MAGENTA + colors.BOLD + " \n Dit is de reden dat je last hebt van prestatie motivatie!  \n" + colors.RESET)
        
        
        break