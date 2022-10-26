# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import codecs
import importlib

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QLineEdit, QScrollArea
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

class Widget(QWidget):
    def __init__(self, parent=None):
        # default display
        super().__init__(parent)
        uic.loadUi('form.ui', self)
        RSA_Items = ["(c,n,e)", "(c,p,q,e)", "(c,n,e,{p or q})", "(c,n,d)", "Hasted Broadcast Attack", "Small Exponent(\"e\") Attack", "Chinese Remainder Theorem", "Fermat Factorization"]
        XOR_Items = ["Single Key", "Repeating Key"]
        self.listOfParams = []
        self.currentBuffer=[]
        self.RSA_Combo.addItems(RSA_Items)
        self.XOR_Combo.addItems(XOR_Items)
        self.RSA_Combo.currentIndexChanged.connect(self.workOnRSA)
        self.XOR_Combo.currentIndexChanged.connect(self.workOnXOR)
        self.NextRSA.clicked.connect(self.submitRSA)
        self.NextXOR.clicked.connect(self.submitXOR)

    def workOnRSA(self):
        print("In WorkOnRSA")
        try:
            self.aboutLabelRSA.setParent(None)
            currentIndex = self.RSA_Combo.currentIndex()
            inputs = {0: ["Ciphertext (in hex)", "N (in hex)", "E (in hex)"],
                      1: ["Ciphertext (in hex)", "P (in hex)", "Q (in hex)", "E (in hex)"],
                      2: ["Ciphertext (in hex)", "N (in hex)", "E (in hex)", "P (in hex)"],
                      3: ["Ciphertext (in hex)", "N (in hex)", "D (in hex)"],
                      4: ["C1 (in hex)", "C2 (in hex)", "C3 (in hex)", "N1 (in hex)", "N2 (in hex)", "N3 (in hex)"],
                      5: ["C (in hex)", "E (in hex)"],
                      6: ["C (in hex)", "P (in hex)", "Q (in hex)", "DP (in hex)", "DQ (in hex)"],
                      7: ["C (in hex)", "N (in hex)", "E (in hex)"]
                      }
            self.clearLayout(self.verticalLayout_4)
            self.currentBuffer.extend(self.addInputsOnIndex(inputs[currentIndex], self.verticalLayout_4))
        except Exception as e:
            print(e)

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
        print("In WorkOnXOR")
        try:
            self.aboutLabelXOR.setParent(None)
            currentIndex = self.XOR_Combo.currentIndex()
            inputs = {0: ["Ciphertext (in hex)"],
                      1: ["Ciphertext (in hex)", "Key (in hex)"]}
            self.clearLayout(self.verticalLayout_5)
            self.currentBuffer.extend(self.addInputsOnIndex(inputs[currentIndex], self.verticalLayout_5))
        except Exception as e:
            print(e)

    def addInputsOnIndex(self, widgets, parent):
        # Expecting labels for QLabels
        listOfInputs = []
        print("In addWidgetsOnIndex")
        try:
            print(widgets, parent)
            for i in widgets:
                layout = QHBoxLayout()
                label = QLabel(i)
                inp = QLineEdit(self)
                layout.addWidget(label)
                layout.addWidget(inp)
                parent.addLayout(layout)
                listOfInputs.append([layout, label, inp])
        except Exception as e:
            print(e)
        return listOfInputs

    def submitRSA(self):
        print("In SubmitInRSA, currentBuffer:", self.currentBuffer)
        funcDict = {i : f"RSA.RSA{i+1}.RSA{i+1}"}
        try:
            currentIndex = self.RSA_Combo.currentIndex()
            variable_list = [codecs.decode(i[2].text(), 'hex') for i in self.currentBuffer]
            mod_name, func_name = funcDict[currentIndex].rsplit('.',1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            res = func(*variable_list)
            out = func(*variable_list)
            result = ScrollLabel()
            result.setText("Result:\n"+str(out))
            self.verticalLayout_4.addWidget(result)
        except Exception as e:
            print(e)

    def submitXOR(self):
        print("In SubmitXOR, currentBuffer:", self.currentBuffer)
        funcDict = {0: "XOR.bruteforce.bruteforce",
                    1: "XOR.repeating_key.repeating_key"}
        try:
            currentIndex = self.XOR_Combo.currentIndex()
            variable_list = [codecs.decode(i[2].text(), 'hex') for i in self.currentBuffer]
            mod_name, func_name = funcDict[currentIndex].rsplit('.',1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            res = func(*variable_list)
            # res = funcDict[currentIndex](*variable_list)
            result = ScrollLabel()
            result.setText("Result:\n"+str(res))
            self.verticalLayout_5.addWidget(result)
        except Exception as e:
            print(e)

        # try:
           # currentIndex = self.XOR_Combo.currentIndex()
           # if currentIndex == 0:
               # inp = codecs.decode(self.currentBuffer[0][2].text(), 'hex')
               # from XOR.bruteforce import bruteforce
               # result = ScrollLabel()
               # result.setText("Result:\n"+str(bruteforce(inp)))
               # self.verticalLayout_5.addWidget(result)
           # elif currentIndex == 1:
               # from XOR.repeating_key import repeating_key
               # result = ScrollLabel()
               # opt1 = codecs.decode(self.currentBuffer[0][2].text(), 'hex')
               # opt2 = codecs.decode(self.currentBuffer[1][2].text(), 'hex')
               # result.setText("Result:\n"+str(repeating_key(opt1, opt2)))
               # self.verticalLayout_5.addWidget(result)
           # else:
                # print("Not implemented")
        # except Exception as e:
           # print(e)
           # msg = QMessageBox()
           # msg.setWindowTitle("Error")
           # msg.setText(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
