def sort_string(string: str) -> str:
    output = string.split()

    # the key parameter allows to make a comparison between 
    # each list item ignoring the capitalizing
    output = sorted(output, key = lambda s: s.upper())
    result = ' '.join(output)
    return result

teste = sort_string("banana ORANGE apple")

print(teste)