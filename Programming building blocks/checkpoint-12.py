people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest=999999
name=''

for person in people:
    person = person.strip().split()
    print(f'Name: {person[0]}, Age: {person[1]}')

    if int(person[1])<int(youngest):
        youngest=person[1]
        name=person[0]

print(f'The youngest person is {name}, and his age is {youngest}')