temperatura_celsius = float(input('Digite a temperatura em ºC: '))

temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32
temperatura_kelvin = (temperatura_celsius + 273.15)

print('A temperatura {:.2f}ºC equivale a {:.2f}ºF e {:.2f}K.'.format(temperatura_celsius, temperatura_fahrenheit, temperatura_kelvin))