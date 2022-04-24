from genericpath import exists
import math
from datetime import datetime

date = datetime.now().date()

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

price = 0
volume = round(
    ((math.pi*width**2*ratio*(width*ratio+2_540*diameter))/10_000_000_000), 2)

if width == 165 and ratio == 65 and diameter == 14:
    price = 128.99
elif width == 175 and ratio == 55 and diameter == 15:
    price = 194.99
elif width == 235 and ratio == 80 and diameter == 16:
    price = 196.99
elif width == 205 and ratio == 75 and diameter == 15:
    price = 103.99
elif width == 305 and ratio == 70 and diameter == 17:
    price = 389.99

print(f'The approximate volume is {volume:.2f} liters')
if price != 0:
    print(f'The price of the tire is: {price:.2f}')

wants_buy = input(
    'Do you want to buy tires with the dimensions that you entered? ').lower()

if wants_buy == 'yes':
    phone_number = input('Enter your phone number: ')

with open('volumes.txt', 'at') as volumes_file:
    if wants_buy == 'yes':
        print(
            f'{date}, {width}, {ratio}, {diameter}, {volume}, {phone_number}', file=volumes_file)
    else:
        print(f'{date}, {width}, {ratio}, {diameter}, {volume}', file=volumes_file)
