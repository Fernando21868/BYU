import csv


def main():
    KEY_COLUMN_INDEX = 0
    products_dict = read_dict('products.csv', KEY_COLUMN_INDEX)
    print(products_dict)
    print()
    with open('request.csv', 'rt') as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for row_list in reader:
            product_number = row_list[0]
            if product_number in products_dict:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = product[2]
                product_quantity = row_list[1]
                print(f"{product_name}: {product_quantity} @ {product_price}")


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

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary


if __name__ == '__main__':
    main()
