"""
Assignment #10 by
    Sandy Nguyen
    06/22/2020
    "Graphical User Interface" Program

Program Description: Allows the user to convert between temperatures in fahrenheit and temperatures in celsius.
"""

import model
import view
import tkinter

class Controller:
    #One object of this class represents the controller, which calls on the appropriate methods in the model.
    def __init__(self):
        #Starts the Tk framework up
        root = tkinter.Tk()
        self.model = model.Temp_Change()
        self.view = view.Frame()
        self.view.convertCel.config(command = self.CeltoF)
        self.view.convertF.config(command = self.FtoCel)
        self.view.mainloop()

    def CeltoF(self):
        #Calls to the CeltoF Function and gets the Celsius variable
        far = self.model.CeltoF(self.view.variableCel.get())
        self.view.variableF.set(far)

    def FtoCel(self):
        #Calls to the FtoCel Function and gets the Farenheit variable
        cel = self.model.FtoCel(self.view.variableF.get())
        self.view.variableCel.set(cel)

if __name__ == "__main__":
    c = Controller()

"""
/Users/sandynguyen/PycharmProjects/assignment_10/venv/bin/python /Users/sandynguyen/PycharmProjects/assignment_10/controller.py
0.0
50.0

Process finished with exit code 0
"""