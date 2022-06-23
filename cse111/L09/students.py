import csv

KEY_COLUMN_INDEX = 0


def main():
    file_name = 'students.csv'
    dictionary = read_dict(file_name, KEY_COLUMN_INDEX)
    print(dictionary)
    user_i_number = input('Please enter an I-Number (xxxxxxxxx): ')
    if user_i_number in dictionary:
        print(dictionary[user_i_number][1])
    else:
        print('No such student')


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            i_number = i[key_column_index]
            dictionary[i_number] = i
    return dictionary


if __name__ == '__main__':
    main()
