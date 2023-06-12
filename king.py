from dictionaries import dictionaries
import colors
import sys

intrinsieke_motivatie = dictionaries['intrinsieke_motivatie']
excentrieke_motivatie = dictionaries['excentrieke_motivatie']
cognitieve_vaardigheden = dictionaries['cognitieve_vaardigheden']
moeilijkheid = dictionaries['moeilijkheid']


print(colors.GREEN + colors.BOLD + "Welkom bij de vragenlijst van de Koning!" + colors.RESET)


def ask_question(question_number, questions_dict, file=None):
    question_id = sorted(questions_dict.keys())[question_number - 1]
    question_text = questions_dict[question_id]
    print(f"{question_number}: {question_text}")
    print(colors.BLUE + "Antwoord met 'ja' of 'nee'" + colors.RESET)
    print(colors.WHITE + "Uw antwoord: " + colors.RESET, end='')
    user_input = input()
    user_input = colors.GREEN + user_input + colors.RESET
    if file:
        file.write(f"{question_number}: {question_text}\n")
        file.write(f"Uw antwoord: {user_input}\n\n")
    return user_input
def validate_ja_nee_answer(answer):
    valid_answers = ["ja", "nee"]
    while answer.lower() not in valid_answers:
        print("Ongeldig antwoord. Vul a.u.b. 'ja' of 'nee' in.")
        answer = input("Uw antwoord" + colors.YELLOW + "ja/nee)" + colors.RESET)
    return answer


def questionnaire():
    userName = input("Give me a name for this file " + colors.RED + "(no spaces)" + colors.RESET + ": ")
    with open(userName +".txt", "w") as file:     
        user_input = ask_question(1, intrinsieke_motivatie)
        if user_input.lower() == "ja":
            for question_number in range(2, len(intrinsieke_motivatie) + 1):
                ask_question(question_number, intrinsieke_motivatie)
        elif user_input.lower() == "nee":
            print("Bye bye!")
    
        else:
            answer = input("Uw antwoord" + colors.YELLOW + "ja/nee)" + colors.RESET)


questionnaire()