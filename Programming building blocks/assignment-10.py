# MILESTONE REQUIREMENTS LESSON 9
name_items = []
price_items = []

shopping_cart = ['bed', 'chair', 'blanket']
items_menu = ['1. Add item', '2. View cart',
              '3. Remove item', '4. Compute total', '5. Modify cart', '6. Quit']
action = ''

while action != 6:
    total_price = 0
    print('Please select one of the following: ')
    for item_menu in items_menu:
        print(item_menu)
    action = int(input('Please enter an action: '))
    if action == 1:
        name_item = input('What item would you like to add? ')
        price_item = float(input(f"What is the price of '{name_item}'? "))
        name_items.append(name_item)
        price_items.append(price_item)
        print(f"'{name_item}' has been added to the cart.")
    elif action == 2:
        print('The contents of the shopping cart are: ')
        for index, name_item in enumerate(name_items):
            price_item=round(price_items[index], 2)
            print(f'{index+1}. {name_item:10} - ${price_item}')
    elif action == 3:
        remove_item = int(input('Which item would you like to remove? '))
        if remove_item > len(name_item):
            print('Sorry, that is not a valid item number.')
        else:
            name_items.pop(remove_item-1)
            price_items.pop(remove_item-1)
            print('Item removed.')
    elif action == 4:
        for price_item in price_items:
            total_price += price_item
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        print(f'The total number of the items are ${len(name_items)}')   
    elif action == 5:
        number_items=int(input('How many items do you want to change from the cart? '))
        for i in range(number_items):
            print(f'The cart has {len(name_items)} items.')
            index_item=int(input(f'{i+1}. Give me the number of item in the cart to modify: '))
            name_item = input('What item would you like to add? ')
            price_item = float(input(f"What is the price of '{name_item}'? "))
            name_items[index_item-1]=name_item
            price_items[index_item-1]=price_item
    elif action == 6:
        print('Thank you. Goodbye.')
    else:
        print('Select a option of the menu.')
    print()
