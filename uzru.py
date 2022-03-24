from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QComboBox,QLabel,QLineEdit
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
# uz=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
# ru=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(250,150,650,235)
		self.setWindowTitle("UZ-RU")
		self.start()
		self.show()
	def font(self,ob):
		ob.setFont(QFont("JetBrains Mono",13))
	def start(self):
		self.line=QLabel("__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __",self)
		self.font(self.line)
		self.line.setGeometry(0,70,800,50)
		self.choose=QComboBox(self)
		self.choose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.font(self.choose)
		self.choose.move(25,30)
		self.choose.addItems(["UZ-RU","RU-UZ"])
		self.place=QLineEdit(self)
		self.place.setPlaceholderText("Matnni kiriting...")
		self.place.setMaxLength(40)
		self.font(self.place)
		self.place.setGeometry(120,30,415,32)
		self.run=QPushButton("RUN",self)
		self.font(self.run)
		self.run.move(550,30)
		self.run.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.words=QLabel("                                                  ",self)
		self.words.move(27,120)
		self.words.setFont(QFont("JetBrains Mono",13))
		self.run.clicked.connect(self.result)
	
	def result(self):
		self.text=str(self.place.text())
		self.words.setText(self.text)
		self.place.setText("")
choose=Window()
sys.exit(app.exec_())