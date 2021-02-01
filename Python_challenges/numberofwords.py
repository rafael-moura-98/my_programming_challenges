def throughTxtFile(txt_file):
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

    
    
throughTxtFile("abcd.txt")