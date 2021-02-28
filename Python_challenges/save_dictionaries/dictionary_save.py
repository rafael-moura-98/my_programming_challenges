my_dictionary = {
    'Rafael': 22, 
    'Carlos': 32,
    'Ana': 25
    }
""" 
def save_dictionary(dic, path):
    with open(f"{path}saved_dictionaries.txt", "w") as f:
        for item in dic.items():
            f.write(str(item[0]))
            f.write(": ")
            f.writelines(str(item[1]))
            f.write("\n")

def load_dictionary(path):
    with open(f"{path}saved_dictionaries.txt", "r") as f:
        info = f.readlines()
        print(info)

save_dictionary(my_dictionary, "")

load_dictionary("") """

import pickle

def save_dictionary(dic, path):
    with open(path, 'wb') as f:
        pickle.dump(dic, f)

def load_dictionary(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

save_dictionary(my_dictionary, "saved_dictionaries.pickle")

info = load_dictionary("saved_dictionaries.pickle")

print(info)