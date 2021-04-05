import pandas as pd
import csv

def csv_to_list(path: str) -> list:
    csv_list = list()

    with open(path, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
        for row in spamreader:
            csv_list.append(row)
        
    return csv_list


def merge_csv_pandas(f1_name = 'a12_mergeCSVFiles\\csvfile1.csv', f2_name = 'a12_mergeCSVFiles\\csvfile2.csv', output_name = None):

    table1 = pd.read_csv(f1_name, header = None )
    table2 = pd.read_csv(f2_name, header = None )

    merged_file = pd.merge(table1, table2, how = 'left')

    #teste do output
    print(merged_file)


def merge_csv(tb1: list, tb2: list, output_name = "Merged_files"):
    set1 = set(tb1[0])
    set2 = set(tb2[0])
    list_difference = list(set2 - set1)

    with open(output_name + ".csv", 'w', newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ';', quotechar = '"')
        spamwriter.writerow(tb1[0] + list_difference)


# Main

table_list_1 = csv_to_list("a12_mergeCSVFiles\\csvfile1.csv")
table_list_2 = csv_to_list("a12_mergeCSVFiles\\csvfile2.csv")

merge_csv(table_list_1, table_list_2)
