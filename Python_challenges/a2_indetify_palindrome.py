def indentify_palindrome(phrase: str) -> bool:
    phrase = phrase.strip()
    phrase = phrase.lower()
    
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.replace(".", "")
    phrase = phrase.replace(";", "")
    phrase = phrase.replace(":", "")
    phrase = phrase.replace("?", "")
    phrase = phrase.replace("!", "")

    phrase_backwards = phrase[::-1]

    if (phrase in phrase_backwards):
        return True
    else:
        return False

palindromo = indentify_palindrome("race car")
print(palindromo)