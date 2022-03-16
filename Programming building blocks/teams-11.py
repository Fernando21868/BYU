names = []
balances = []

print('Enter the names and balances of bank accounts (type: quit when done)')
account_name=input('What is the name of this account? ')

while account_name.lower()!='quit':
    names.append(account_name)
    account_balance=float(input('What is the balance? '))
    balances.append(account_balance)
    account_name=input('What is the name of this account? ')

print('\nAccount information: ')
for i in range(len(names)):
    print(f'{i+1}. {names[i]} - ${balances[i]:.2f}')

highest=max(balances)
index=balances.index(highest)
name_highest=names[index]

print(f'\nTotal: ${sum(balances)}')
print(f'Avarage: ${sum(balances)/len(balances):.2f}')
print(f'Highest balance: {name_highest} - ${highest}')



update_account=input('\nDo you want to update an account? ')
while update_account.lower()=='yes':
    index_update=int(input('What account index do you want to update? '))
    new_amount=float(input('What is the new amount? '))
    balances[index_update-1]=new_amount
    print('\nAccount information: ')
    for i in range(len(names)):
        print(f'{i+1}. {names[i]} - ${balances[i]:.2f}')
    
    update_account=input('\nDo you want to update an account? ')

print('\nAccount information: ')
for i in range(len(names)):
    print(f'{i+1}. {names[i]} - ${balances[i]:.2f}')
