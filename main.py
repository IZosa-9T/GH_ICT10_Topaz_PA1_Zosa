# Conditional statements in python

from pyscript import display, document, window

def Convert_and_Check(e):
    document.getElementById('output').innerHTML = ' '

    Celsius = float(document.getElementById('InputTemperature').value)
    Farenheitunrounded = float(Celsius * (9/5) + 32)
    Farenheit = round(Farenheitunrounded, 2)

    if Farenheit >= 37.8:
        display(f'Your temperature in Farenheit is {Farenheit}. Rest well, for your temperature indicates a fever.', target='output')
    else:
        display(f'Your temperature in Farenheit is {Farenheit}. Best maintain it, a healthy number isn\'t always common.', target='output')