import csv
from datetime import datetime


def main():
    # Variables
    current_date_and_time = datetime.now()
    number_items = 0
    subtotal = 0
    total = 0
    tax = 0.06
    sales_taxt = 0

    # Constants
    KEY_COLUMN_INDEX = 0
    products_dict = read_dict('products.csv', KEY_COLUMN_INDEX)

    print('Inkom Emporium')

    try:
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
                    number_items += int(product_quantity)
                    subtotal += (float(product_price)*int(product_quantity))
        sales_taxt = subtotal*tax
        total = subtotal+sales_taxt

        # Exceds requirements
        name_week = current_date_and_time.today().strftime('%A')
        current_time = current_date_and_time.today().strftime('%H')
        if name_week == 'Tuesday' or name_week == 'Wednesday':
            total = total-(total*0.1)
        elif int(current_time) < 11:
            total = total-(total*0.1)
    # Excepts
    except KeyError as key_err:
        print('Error: unknown product ID in the request.csv file')
        print(key_err)
    except FileNotFoundError as err_file:
        print(err_file)
    except PermissionError as err_perm:
        print(err_perm)

    # Output
    print()
    print('Number of Items:', number_items)
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Sales Tax: {sales_taxt:.2f}')
    print(f'Total: {total:.2f}')
    print()
    print('Thank you for shopping at the Inkom Emporium.')
    print(f"{current_date_and_time:%a %b %e %H:%M:%S %Y}")


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
