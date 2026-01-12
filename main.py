# Conditional statements in python

from pyscript import display, document, window

def Convert_and_Check(e):
    document.getElementById('output').innerHTML = ' '

    Farenheit = float(document.getElementById('InputTemperature').value)
    Celsiusunrounded = float((Farenheit - 32) * (5/9))
    Celsius = round(Celsiusunrounded, 2)

    if Celsius >= 37.8:
        display(f'Your temperature in Farenheit is {Celsius}. Rest well, for your temperature indicates a fever.', target='output')
    else:
        display(f'Your temperature in Farenheit is {Celsius}. Best maintain it, a healthy number isn\'t always common.', target='output')
