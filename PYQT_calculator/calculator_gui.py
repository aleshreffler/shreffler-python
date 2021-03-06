# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 393)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.memoryCB = QtWidgets.QComboBox(Form)
        self.memoryCB.setObjectName("memoryCB")
        self.verticalLayout.addWidget(self.memoryCB)
        self.numberLE = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberLE.sizePolicy().hasHeightForWidth())
        self.numberLE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberLE.setFont(font)
        self.numberLE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberLE.setObjectName("numberLE")
        self.verticalLayout.addWidget(self.numberLE)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plusPB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusPB.sizePolicy().hasHeightForWidth())
        self.plusPB.setSizePolicy(sizePolicy)
        self.plusPB.setObjectName("plusPB")
        self.horizontalLayout_2.addWidget(self.plusPB)
        self.minusPB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusPB.sizePolicy().hasHeightForWidth())
        self.minusPB.setSizePolicy(sizePolicy)
        self.minusPB.setObjectName("minusPB")
        self.horizontalLayout_2.addWidget(self.minusPB)
        self.equalPB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalPB.sizePolicy().hasHeightForWidth())
        self.equalPB.setSizePolicy(sizePolicy)
        self.equalPB.setObjectName("equalPB")
        self.horizontalLayout_2.addWidget(self.equalPB)
        self.clearPB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearPB.sizePolicy().hasHeightForWidth())
        self.clearPB.setSizePolicy(sizePolicy)
        self.clearPB.setObjectName("clearPB")
        self.horizontalLayout_2.addWidget(self.clearPB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.digit8PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit8PB.sizePolicy().hasHeightForWidth())
        self.digit8PB.setSizePolicy(sizePolicy)
        self.digit8PB.setObjectName("digit8PB")
        self.gridLayout.addWidget(self.digit8PB, 0, 1, 1, 1)
        self.digit7PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit7PB.sizePolicy().hasHeightForWidth())
        self.digit7PB.setSizePolicy(sizePolicy)
        self.digit7PB.setObjectName("digit7PB")
        self.gridLayout.addWidget(self.digit7PB, 0, 0, 1, 1)
        self.digit9PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit9PB.sizePolicy().hasHeightForWidth())
        self.digit9PB.setSizePolicy(sizePolicy)
        self.digit9PB.setObjectName("digit9PB")
        self.gridLayout.addWidget(self.digit9PB, 0, 2, 1, 1)
        self.digit4PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit4PB.sizePolicy().hasHeightForWidth())
        self.digit4PB.setSizePolicy(sizePolicy)
        self.digit4PB.setObjectName("digit4PB")
        self.gridLayout.addWidget(self.digit4PB, 1, 0, 1, 1)
        self.digit5PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit5PB.sizePolicy().hasHeightForWidth())
        self.digit5PB.setSizePolicy(sizePolicy)
        self.digit5PB.setObjectName("digit5PB")
        self.gridLayout.addWidget(self.digit5PB, 1, 1, 1, 1)
        self.digit6PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit6PB.sizePolicy().hasHeightForWidth())
        self.digit6PB.setSizePolicy(sizePolicy)
        self.digit6PB.setObjectName("digit6PB")
        self.gridLayout.addWidget(self.digit6PB, 1, 2, 1, 1)
        self.digit2PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit2PB.sizePolicy().hasHeightForWidth())
        self.digit2PB.setSizePolicy(sizePolicy)
        self.digit2PB.setObjectName("digit2PB")
        self.gridLayout.addWidget(self.digit2PB, 2, 1, 1, 1)
        self.digit1PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit1PB.sizePolicy().hasHeightForWidth())
        self.digit1PB.setSizePolicy(sizePolicy)
        self.digit1PB.setObjectName("digit1PB")
        self.gridLayout.addWidget(self.digit1PB, 2, 0, 1, 1)
        self.digit3PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit3PB.sizePolicy().hasHeightForWidth())
        self.digit3PB.setSizePolicy(sizePolicy)
        self.digit3PB.setObjectName("digit3PB")
        self.gridLayout.addWidget(self.digit3PB, 2, 2, 1, 1)
        self.digit0PB = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit0PB.sizePolicy().hasHeightForWidth())
        self.digit0PB.setSizePolicy(sizePolicy)
        self.digit0PB.setObjectName("digit0PB")
        self.gridLayout.addWidget(self.digit0PB, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numberLE.setText(_translate("Form", "0"))
        self.plusPB.setText(_translate("Form", "+"))
        self.minusPB.setText(_translate("Form", "-"))
        self.equalPB.setText(_translate("Form", "="))
        self.clearPB.setText(_translate("Form", "Clear"))
        self.digit8PB.setText(_translate("Form", "8"))
        self.digit7PB.setText(_translate("Form", "7"))
        self.digit9PB.setText(_translate("Form", "9"))
        self.digit4PB.setText(_translate("Form", "4"))
        self.digit5PB.setText(_translate("Form", "5"))
        self.digit6PB.setText(_translate("Form", "6"))
        self.digit2PB.setText(_translate("Form", "2"))
        self.digit1PB.setText(_translate("Form", "1"))
        self.digit3PB.setText(_translate("Form", "3"))
        self.digit0PB.setText(_translate("Form", "0"))

