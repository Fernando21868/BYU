from unicodedata import name


names = []
name_friend = ''

while name_friend != 'end':
    name_friend = input('Type the name of a friend: ')
    if name_friend != 'end':
        names.append(name_friend)

print('Your friends are: ')
for name_friend in names:
    print(name_friend)
