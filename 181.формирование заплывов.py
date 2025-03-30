import sys
import csv
from collections import OrderedDict


def main():
    #загрузка csv-файла
    with open(r'heats.csv', encoding='utf-8') as r_file:
        #создаем объект reader
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        # считываем
        dictionary = {'1': '4', '2': '5', '3': '3', '4': '6', '5': '2', '6': '7', '7': '1', '8': '8'}
        late_dict = dict()
        my_dict = dict()
        for row in file_reader:
            if row[0] == '0':
                late_dict[float(row[2])] = row[1]
            if row[2] != 'time':
                my_dict[float(row[2])] = row[1]
        sorted_dict = OrderedDict(reversed(sorted(my_dict.items())))
        i = 1
        for key, value in late_dict.items():
            if int(list(sorted_dict).index(key) + 1) % 8 == 0:
                print(f'{value},{(int(list(sorted_dict).index(key)) + 1) // 8},{dictionary['1']}')
            else:
                print(f'{value},{(int(list(sorted_dict).index(key))+ 1) // 8 + 1},{dictionary[str(9 - ((int(list(sorted_dict).index(key)) + 1) % 8))]}')
    pass


if __name__ == '__main__':
    main()
