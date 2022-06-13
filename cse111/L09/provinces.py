from operator import le


list_provinces = []
with open('provinces.txt', 'rt') as provinces:
    for province in provinces:
        clean_line = province.strip()
        list_provinces.append(clean_line)
print(list_provinces)
print(list_provinces.pop(0))
print(list_provinces.pop())
count = 0
for i in range(len(list_provinces)):
    if list_provinces[i] == 'AB' or list_provinces[i] == 'Alberta':
        count += 1
    if list_provinces[i] == 'AB':
        list_provinces[i] = 'Alberta'

print(count)
print(list_provinces)
print(list_provinces.count('Alberta'))
