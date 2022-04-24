import math

number_items = int(input('Enter the number of items: '))
number_items_box = int(input('Enter the number of items per box: '))

boxes = math.ceil(number_items/number_items_box)

print(f'For {number_items} items, packing {number_items_box} items in each box, you will need {boxes} boxes.')
