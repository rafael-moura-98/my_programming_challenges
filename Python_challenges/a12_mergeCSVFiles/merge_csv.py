import csv

def csv_to_list(path: str) -> list:
    csv_list = list()

    with open(path, 'r', newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in spamreader:
            csv_list.append(row)
        
    return csv_list


def merge_csv(f1_name, f2_name, output_name = None):

    csv1 = csv_to_list(f1_name)
    csv2 = csv_to_list(f2_name)

        
    print(csv1)
    print(" ")
    print(csv2)

merge_csv("mergeCSVFiles\\csvfile1.csv", "mergeCSVFiles\\csvfile2.csv")
