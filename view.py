"""
Assignment #10 by
    Sandy Nguyen
    06/22/2020
    "Graphical User Interface" Program

Program Description: Allows the user to convert between temperatures in fahrenheit and temperatures in celsius.
"""

import tkinter
import model

class Frame(tkinter.Frame):
    #One object of this class represents the tkinter frame view for the architecture of the program.
    def __init__(self):
        #Creates the frame
        tkinter.Frame.__init__(self)
        self.pack()

        #Labels celsius and sets it
        self.labelCel = tkinter.Label(self, text = "Celsius")
        self.labelCel.grid(row=0, column=0)
        self.variableCel = tkinter.DoubleVar()

        #Takes the input of celsius
        self.entryCel = tkinter.Entry(self, textvariable=self.variableCel)
        print(self.variableCel.get())
        self.entryCel.grid(row=1, column=0)

        #Labels farenheit and sets it
        self.labelF = tkinter.Label(self, text= "Farenheit")
        self.labelF.grid(row=0, column=2)
        self.variableF = tkinter.DoubleVar()

        #Takes the input of farenheit
        self.entryF = tkinter.Entry(self, textvariable=self.variableF)
        self.entryF.grid(row=1, column=2)

        #Converts Cel to F
        self.convertCel = tkinter.Button(self, text = "Cel to Far")
        self.convertCel.grid(row=0, column=1)

        #Converts Cel to F
        self.convertF = tkinter.Button(self, text="Far to Cel")
        self.convertF.grid(row=1, column=1)