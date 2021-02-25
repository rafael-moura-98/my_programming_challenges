from random import randint


def generate_pass(number_of_words):
    with open("C:\\Workspace\\my_programming_challenges\\"+
    "Python_challenges\\diceware\\portuguese_words.txt", "r", encoding="utf8") as words:
        
        content = words.readlines()

    password = ""
    for i in range(number_of_words):
        chosen_word = randint(0, 309000)
        password += str(content[chosen_word]).replace("\n", " ")

    print(password)

generate_pass(5)