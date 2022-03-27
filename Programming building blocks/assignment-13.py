def calculate_temeperature(temperature, wind_speed, type_temperature='F'):
    T = temperature
    if type_temperature == 'C':
        T = (temperature*(9/5))+32
    V = wind_speed
    wind_child = 35.74 + (0.6215*T) - (35.75*(V**0.16)) + \
        ((0.4275*T)*(V**0.16))
    print(
        f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_child:.2f}F')


def iterate_loop_for(type_temperature):
    if type_temperature == 'F':
        for i in range(5, 61, 5):
            calculate_temeperature(temperature, i)
    elif type_temperature == 'C':
        for i in range(5, 61, 5):
            calculate_temeperature(temperature, i, type_temperature)
    else:
        print('Please enter a correct type of temperature.')


temperature = float(input('What is the temperature? '))
type_temperature = input('Fahrenheit or Celsius (F/C)? ').upper()
iterate_loop_for(type_temperature)
