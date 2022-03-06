items=[]
item=None

print('Please enter the items of the shopping list (type: quit to finish): ')

while item.lower() != 'quit':
    item=input('Item: ')
    if item.lower()!='quit':
        items.append(item)
print()

print('The shopping list is: ')
for i in items:
    print(item)
print()


print('The shopping list with indexes is: ')
for i in range(len(items)):
    print(f'{i}. {items[i]}')
print()


index_new_item=int(input('Which item would you like to change? '))
new_item=input('What is the new item? ')
print()


items.pop(index_new_item)
items.insert(index_new_item, new_item)
# items[index_new_item]=new_item

print('The shopping list with indexes is: ')
for i in range(len(items)):
    print(f'{i}. {items[i]}')