from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(295, 258)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #890F0D")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 71, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: #051367")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 40, 71, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: #361500")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 100, 71, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: #085E7D")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 100, 71, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background-color: #B3541E")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 100, 71, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color: #35858B")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 160, 71, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("background-color: #9A0680")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 160, 71, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("background-color: #064635")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 160, 71, 61))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("background-color: #890F0D")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.hide()

        self.pushButton_8.clicked.connect(self.b1)
        self.pushButton_6.clicked.connect(self.b2)
        self.pushButton_7.clicked.connect(self.b3)
        self.pushButton_5.clicked.connect(self.b4)
        self.pushButton_3.clicked.connect(self.b5)
        self.pushButton_2.clicked.connect(self.b6)
        self.pushButton_4.clicked.connect(self.b7)
        self.pushButton_9.clicked.connect(self.b8)
        self.pushButton.clicked.connect(self.b9)
    
    def b1(self, Form):
        if self.pushButton_9.text()=="":
            self.pushButton_9.setText("8")
            self.pushButton_9.show()
            self.pushButton_8.setText("")
            self.pushButton_8.hide()
        else:
            pass

    def b2(self, Form):
        if self.pushButton_9.text()=="":
            self.pushButton_9.setText("6")
            self.pushButton_9.show()
            self.pushButton_6.setText("")
            self.pushButton_6.hide()
        else:
            pass

    def b3(self, Form):
        if self.pushButton_8.text()=="":
            self.pushButton_8.setText("7")
            self.pushButton_8.show()
            self.pushButton_7.setText("")
            self.pushButton_7.hide()
        else:
             pass

    def b4(self, Form):
        if self.pushButton_8.text()=="":
            self.pushButton_8.setText("5")
            self.pushButton_8.show()
            self.pushButton_5.setText("")
            self.pushButton_5.hide()
        else:
            pass

    def b5(self, Form):
        if self.pushButton_6.text()=="":
            self.pushButton_6.setText("3")
            self.pushButton_6.show()
            self.pushButton_3.setText("")
            self.pushButton_3.hide()
        else:
            pass

    def b6(self, Form):
        if self.pushButton_3.text()=="":
            self.pushButton_3.setText("2")
            self.pushButton_3.show()
            self.pushButton_2.setText("")
            self.pushButton_2.hide()
        else:
            pass

    def b7(self, Form):
        if self.pushButton_7.text()=="":
            self.pushButton_7.setText("4")
            self.pushButton_7.show()
            self.pushButton_4.setText("")
            self.pushButton_4.hide()
        else:
            pass

    def b8(self, Form):
        if self.pushButton_8.text()=="":
            self.pushButton_8.setText("8")
            self.pushButton_8.show()
            self.pushButton_9.setText("")
            self.pushButton_9.hide()
        else:
            pass

    def b9(self, Form):
        if self.pushButton_4.text()=="":
            self.pushButton_4.setText("1")
            self.pushButton_4.show()
            self.pushButton.setText("")
            self.pushButton.hide()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())