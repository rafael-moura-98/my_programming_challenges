from random import randint


def generate_pass(number_of_words):
    """
    It return a random phrase to help create a strong password. The words come from a vast list of brazillian portuguese words.

    Source of found words https://github.com/pythonprobr/palavras

    Parameter
    ---------

    password: number of words to be returned
    """
    with open("a11_diceware\\portuguese_words.txt", "r", encoding="utf8") as words:
        
        content = words.readlines()

    password = ""
    for i in range(number_of_words):
        chosen_word = randint(0, 309000)
        password += str(content[chosen_word]).replace("\n", " ")

    print(password)

generate_pass(5)