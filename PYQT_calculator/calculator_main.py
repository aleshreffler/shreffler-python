# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QWidget

import calculator_gui


# auxiliary functions

def digitClicked(number):
    """update line edit widget with a new digit given in parameter number"""
    global numberEntered
    
    text = ui.numberLE.text()            # get current text of input widget
    if text == "0" or not numberEntered: # if this is the first digit entered or the number currently is 0, start with an empty string instead
       text = ""
    text += str(number)                  # add digit to text
    ui.numberLE.setText(text)            # update content of line edit widget
    numberEntered = True
    
def evaluateResult():
    """process last operation that was entered and update GUI accordingly"""
    number = int(ui.numberLE.text())     # get current number from line edit widget
    
    global lastOperation
    global intermediateResult
    global numberEntered

    if lastOperation and numberEntered:  # only perform operation if a operation button has been clicked and a new number has been added since
        if lastOperation == "+":         # perform copmutation
            intermediateResult += number
        elif lastOperation == "-":
            intermediateResult -= number
        ui.numberLE.setText(str(intermediateResult)) # update line edit widget with new result
        ui.memoryCB.addItem(str(intermediateResult)) # add new result as item to memory combo box
    else:
        intermediateResult = number

    numberEntered = False
    
def operatorClicked(operation):
    """process new operation by peforming the last one and updating variable lastOperation"""
    evaluateResult()          # perform previous operation (if any)
    
    global lastOperation      # update global variable lastOperation to operation whose button was just clicked
    lastOperation = operation 


# event handler functions

def digit0PBClicked(): # when a digit button is clicked we simply call digitClicked() with the respective number
    digitClicked(0)
    
def digit1PBClicked():
    digitClicked(1)
    
def digit2PBClicked():
    digitClicked(2)
    
def digit3PBClicked():
    digitClicked(3)
    
def digit4PBClicked():
    digitClicked(4)
    
def digit5PBClicked():
    digitClicked(5)
    
def digit6PBClicked():
    digitClicked(6)
    
def digit7PBClicked():
    digitClicked(7)
    
def digit8PBClicked():
    digitClicked(8)
    
def digit9PBClicked():
    digitClicked(9)
    
    
def plusPBClicked():     # when an operation button is clicked we simply call operatorClicked with a string representing the operation
    operatorClicked("+")

def minusPBClicked():
    operatorClicked("-")
    
    
def equalPBClicked():    # when the equal button is clicked we just have to call evaluateResult()
    evaluateResult()

def clearPBClicked():    # when the clear button is clicked we just reset the global variables and GUI
    global lastOperation
    global intermediateResult
    global numberEntered
    lastOperation = None
    intermediateResult = 0
    numberEntered = False
    ui.numberLE.setText("0")   # set content of line edit widget back to "0"

def memoryCBActivated():  # when an entry from the memory combo is selected, we use it for the content of the line edit widget
    text = ui.memoryCB.currentText() # get selected item from combo box
    ui.numberLE.setText(text) # update content of line edit widget with number
    global numberEntered
    numberEntered = True      # update global variable to reflect that a new number has been entered

# set up global variables needed

intermediateResult = 0  # used to store current result 
numberEntered = False   # True if user has entered a digit after the last time +,-,= or clear was pressed
lastOperation = None    # last operation button that was clicked

# create application and gui

app = QApplication(sys.argv)

mainWindow = QWidget()        # create an instance of QWidget for the main window
ui = calculator_gui.Ui_Form() # create an instance of the GUI class from calculator_gui.py
ui.setupUi(mainWindow)        # create the GUI for the main window

# connect event handler functions

ui.digit0PB.clicked.connect(digit0PBClicked) # connect each digit button to corresponding function
ui.digit1PB.clicked.connect(digit1PBClicked)
ui.digit2PB.clicked.connect(digit2PBClicked)
ui.digit3PB.clicked.connect(digit3PBClicked)
ui.digit4PB.clicked.connect(digit4PBClicked)
ui.digit5PB.clicked.connect(digit5PBClicked)
ui.digit6PB.clicked.connect(digit6PBClicked)
ui.digit7PB.clicked.connect(digit7PBClicked)
ui.digit8PB.clicked.connect(digit8PBClicked)
ui.digit9PB.clicked.connect(digit9PBClicked)

ui.plusPB.clicked.connect(plusPBClicked)     # connect each operator button to corresponding function
ui.minusPB.clicked.connect(minusPBClicked)

ui.equalPB.clicked.connect(equalPBClicked)       # connect equal button
ui.clearPB.clicked.connect(clearPBClicked)       # connect clear button

ui.memoryCB.activated.connect(memoryCBActivated) # connect memory combox box activated signal emitted 
                                                 #   when use selects an entry from the memory combo box

# run app

mainWindow.show()
sys.exit(app.exec_())