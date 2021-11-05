import sys

from PyQt5.QtWidgets import QApplication, QWidget

import calculator_gui

# create application and gui

app = QApplication(sys.argv)

mainWindow = QWidget()        # create an instance of QWidget for the main window
ui = calculator_gui.Ui_Form() # create an instance of the GUI class from calculator_gui.py
ui.setupUi(mainWindow)        # create the GUI for the main window

# run app

mainWindow.show()
sys.exit(app.exec_())