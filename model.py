"""
Assignment #10 by
    Sandy Nguyen
    06/22/2020
    "Graphical User Interface" Program

Program Description: Allows the user to convert between temperatures in fahrenheit and temperatures in celsius.
"""

class Temp_Change:
    #One object of this class represents the temperature change model.

    def CeltoF(self, value):
        #Does the algebraic conversion of Celsius to Farenheit
        try:
            print(value)
            return (9.0/5.0 * value + 32)
        except:
            print("Error while calculating.")

    def FtoCel(self, value):
        #Does the algebraic conversion of Farenheit to Celsius
        try:
            return ((value-32) * (5.0/9.0))
        except:
            print("Error while calculating.")