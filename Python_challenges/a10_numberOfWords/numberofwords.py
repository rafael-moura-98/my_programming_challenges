def throughTxtFile(txt_file: str) -> int:
    """Prints the number of words in a txt file.

    Parameters
    ----------
    txt_file : str
        The file location of the text. (File must be a txt file)

    Returns
    -------
    Int
        Number of found words in the passed file.
    """

    with open(txt_file, 'r') as f:
        info = f.readlines()

    textInfo = " ".join(info)
    wordsQuantity = len(textInfo.split())
    txtWords = textInfo.split()
    firstTwentyWords = dict()

    for word in txtWords:
        if(word in firstTwentyWords):
            firstTwentyWords[word] += 1
        else:
            firstTwentyWords[word] = 1

    #print
    print(f"Há {wordsQuantity} palavras nesse documento.", end="\n\n")

    
    
throughTxtFile("C:\\Workspace\\my_programming_challenges\\Python_challenges\\numberOfWords\\abcd.txt")
