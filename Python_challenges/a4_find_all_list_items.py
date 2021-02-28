#[[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
 
def find_items(vlist: list, value: str) -> list:
    result = list()

    for count, a in enumerate(vlist):
        if isinstance(a, list):
            for index in find_items(a, value): #[0]
                result.append([count, index])
        elif a == value:
            result.append(count)

    return result

teste = find_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)

print(teste)