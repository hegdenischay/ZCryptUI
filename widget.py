# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import codecs
import importlib

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QLineEdit, QScrollArea, QMainWindow, QAction, QComboBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile
from PyQt5 import uic

#from PyQt5.QtUiTools import QUiLoader
class ScrollLabel(QScrollArea):
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        # making widget resizable
        self.setWidgetResizable(True)
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
        # vertical box layout
        lay = QVBoxLayout(content)
        # creating label
        self.label = QLabel(content)
        # making label multi-line
        self.label.setWordWrap(True)
        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class Widget(QMainWindow):
    def __init__(self, parent=None):
        # default display
        super().__init__(parent)
        uic.loadUi('/home/nhegde/not-required/ZCryptZip/form.ui', self)
        aboutButton = QAction(QIcon('exit24.png'), 'About', self)
        aboutButton.setStatusTip('About application')
        aboutButton.triggered.connect(self.showAbout)
        self.menu_About.addAction(aboutButton)
        RSA_Items = ["(c,n,e)", "(c,p,q,e)", "(c,n,e,{p or q})", "(c,n,d)", "Hasted Broadcast Attack", "Small Exponent(\"e\") Attack", "Chinese Remainder Theorem", "Fermat Factorization"]
        XOR_Items = ["Single Key", "Repeating Key"]
        self.listOfParams = []
        self.currentBuffer=[]
        self.RSA_Combo.addItems(RSA_Items)
        self.XOR_Combo.addItems(XOR_Items)
        self.tabWidget.currentChanged.connect(self.tabChanges)
        self.workOnRSA()
        self.RSA_Combo.currentIndexChanged.connect(self.workOnRSA)
        self.XOR_Combo.currentIndexChanged.connect(self.workOnXOR)
        self.NextRSA.clicked.connect(self.submitRSA)
        self.NextXOR.clicked.connect(self.submitXOR)

    def tabChanges(self, i):
        if i == 0:
            self.workOnRSA()
        elif i == 1:
            self.workOnXOR()
        else:
            print("Exception")

    def showAbout(self):
        aboutBox = QMessageBox(self)
        aboutBox.setWindowTitle("About application")
        aboutBox.setText("ZCrypt in PyQt5.\nConsole version coded by stoic3r, GUI by @thatloststudent")
        aboutBox.show()

    def showWarningBox(self, error):
        warningBox = QMessageBox(self)
        warningBox.setIcon(QMessageBox.Critical)
        warningBox.setWindowTitle("Error!")
        warningBox.setText(str(error))
        warningBox.show()

    def workOnRSA(self):
        try:
            self.aboutLabelRSA.setParent(None)
            currentIndex = self.RSA_Combo.currentIndex()
            inputs = {0: ["Ciphertext", "N", "E"],
                      1: ["Ciphertext", "P", "Q", "E"],
                      2: ["Ciphertext", "N", "E", "P"],
                      3: ["Ciphertext", "N", "D"],
                      4: ["C1", "C2", "C3", "N1", "N2", "N3"],
                      5: ["C", "E"],
                      6: ["C", "P", "Q", "DP", "DQ"],
                      7: ["C", "N", "E"]
                      }
            self.clearLayout(self.verticalLayout_4)
            self.currentBuffer.extend(self.addInputsOnIndex(inputs[currentIndex], self.verticalLayout_4))
        except Exception as e:
            self.showWarningBox(e)

    def clearLayout(self, layout):
        if layout is not None:
            while len(layout) > 0:
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.clearLayout(item.layout())
        self.currentBuffer = []

    def workOnXOR(self):
        try:
            self.aboutLabelXOR.setParent(None)
            currentIndex = self.XOR_Combo.currentIndex()
            inputs = {0: ["Ciphertext"],
                      1: ["Ciphertext", "Key"]}
            self.clearLayout(self.verticalLayout_5)
            self.currentBuffer.extend(self.addInputsOnIndex(inputs[currentIndex], self.verticalLayout_5))
        except Exception as e:
            self.showWarningBox(e)

    def addInputsOnIndex(self, widgets, parent):
        # Expecting labels for QLabels
        listOfInputs = []
        try:
            layout = QGridLayout()
            for i in range(len(widgets)):
                label = QLabel(widgets[i])
                comboItems = ["Hex", "Decimal"]
                combo = QComboBox()
                combo.addItems(comboItems)
                inp = QLineEdit(self)
                layout.addWidget(label, i, 0)
                layout.addWidget(combo, i, 1)
                layout.addWidget(inp, i, 2)
                parent.addLayout(layout)
                listOfInputs.append([layout, label, combo, inp])
        except Exception as e:
            print(e)
            self.showWarningBox(e)
        return listOfInputs

    def submitRSA(self):
        funcDict = {i : f"RSA.RSA{i+1}.RSA{i+1}" for i in range(9)}
        try:
            currentIndex = self.RSA_Combo.currentIndex()
            variable_list = [int(i[3].text(), 16) if i[2].currentIndex() == 0 else int(i[3].text())  for i in self.currentBuffer]
            mod_name, func_name = funcDict[currentIndex].rsplit('.',1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            res = func(*variable_list)
            out = func(*variable_list)
            result = ScrollLabel()
            result.setText("Result:\n"+str(out))
            self.verticalLayout_4.addWidget(result)
        except Exception as e:
            self.showWarningBox(e)

    def submitXOR(self):
        funcDict = {0: "XOR.bruteforce.bruteforce",
                    1: "XOR.repeating_key.repeating_key"}
        try:
            currentIndex = self.XOR_Combo.currentIndex()
            variable_list = [codecs.decode(i[3].text(), 'hex') if i[2].currentIndex() == 0 else int(i[3].text()) for i in self.currentBuffer]
            mod_name, func_name = funcDict[currentIndex].rsplit('.',1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            res = func(*variable_list)
            # res = funcDict[currentIndex](*variable_list)
            result = ScrollLabel()
            result.setText("Result:\n"+str(res))
            self.verticalLayout_5.addWidget(result)
        except Exception as e:
            self.showWarningBox(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
