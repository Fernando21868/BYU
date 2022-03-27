from email import message


def display_regular(message_u):
    print(message_u)


def display_uppercase(message_u):
    print(message_u.upper())


def display_lowercase(message_u):
    print(message_u.lower())


message_user = input('What is your message? ')
display_regular(message_user)
display_uppercase(message_user)
display_lowercase(message_user)
