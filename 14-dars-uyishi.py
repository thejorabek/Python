# 1-MASALA

# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# from PyQt5.QtGui import QFont
# import sys

# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(300,300,400,300)
# 		self.setWindowTitle("Button")
# 		self.button()
# 		self.show()
# 	def font(self,_font):
# 		_font.setFont(QFont("JetBrains Mono",13))
# 	def button(self):
# 		p1=QPushButton("up",self)
# 		self.font(p1)
# 		p1.setGeometry(165,155,60,60)
# 		p2=QPushButton("down",self)
# 		self.font(p2)
# 		p2.setGeometry(165,220,60,60)
# 		p3=QPushButton("left",self)
# 		self.font(p3)
# 		p3.setGeometry(100,220,60,60)
# 		p4=QPushButton("right",self)
# 		self.font(p4)
# 		p4.setGeometry(230,220,60,60)
# 		self.p5=QPushButton("+",self)
# 		self.font(self.p5)
# 		self.p5.setGeometry(180,70,30,30)
# 		self.u=QPushButton("",self)
# 		self.font(self.u)
# 		self.u.setGeometry(180,30,30,30)
# 		self.u.hide()
# 		self.d=QPushButton("",self)
# 		self.font(self.d)
# 		self.d.setGeometry(180,110,30,30)
# 		self.d.hide()
# 		self.l=QPushButton("",self)
# 		self.font(self.l)
# 		self.l.setGeometry(220,70,30,30)
# 		self.l.hide()
# 		self.r=QPushButton("",self)
# 		self.font(self.r)
# 		self.r.setGeometry(140,70,30,30)
# 		self.r.hide()
# 		p1.clicked.connect(self.tepa)
# 		p2.clicked.connect(self.past)
# 		p3.clicked.connect(self.chap)
# 		p4.clicked.connect(self.ong)

# 	def tepa(self):
# 		self.d.hide()
# 		self.l.hide()
# 		self.r.hide()
# 		self.p5.hide()
# 		self.u.setText("+")
# 		self.u.show()
# 	def past(self):
# 		self.p5.hide()
# 		self.u.hide()
# 		self.l.hide()
# 		self.r.hide()
# 		self.d.setText("+")
# 		self.d.show()
# 	def ong(self):
# 		self.p5.hide()
# 		self.u.hide()
# 		self.d.hide()
# 		self.r.hide()
# 		self.l.setText("+")
# 		self.l.show()
# 	def chap(self):
# 		self.p5.hide()
# 		self.u.hide()
# 		self.l.hide()
# 		self.d.hide()
# 		self.r.setText("+")
# 		self.r.show()

# window=Window()
# sys.exit(app.exec_())


# 2-MASALA

# from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
# import sys

# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(425,200,230,300)
# 		self.setWindowTitle("Game")
# 		self.button()
# 		self.show()
# 	def button(self):
# 		self.b1=QPushButton("",self)
# 		self.b1.setGeometry(50,50,50,50)
# 		self.b2=QPushButton("",self)
# 		self.b2.setGeometry(50,130,50,50)
# 		self.b3=QPushButton("",self)
# 		self.b3.setGeometry(50,210,50,50)
# 		self.b4=QPushButton("",self)
# 		self.b4.setGeometry(130,50,50,50)
# 		self.b5=QPushButton("",self)
# 		self.b5.setGeometry(130,130,50,50)
# 		self.b6=QPushButton("",self)
# 		self.b6.setGeometry(130,210,50,50)

# 		self.b1.clicked.connect(self.click1)
# 		self.b2.clicked.connect(self.click2)
# 		self.b3.clicked.connect(self.click3)
# 		self.b4.clicked.connect(self.click4) 
# 		self.b5.clicked.connect(self.click5)
# 		self.b6.clicked.connect(self.click6)

# 	def click1(self):
# 			self.b1.setText("1")
# 			if self.b1.text()==self.b5.text():
# 				self.b1.hide()
# 				self.b5.hide()

# 	def click2(self):
# 			self.b2.setText("3")
# 			if self.b2.text()==self.b6.text():
# 				self.b2.hide()
# 				self.b6.hide()
# 	def click3(self):
# 			self.b3.setText("2")
# 			if self.b3.text()==self.b4.text():
# 				self.b3.hide()
# 				self.b4.hide()
# 	def click4(self):
# 			self.b4.setText("2")
# 			if self.b4.text()==self.b3.text():
# 				self.b4.hide()
# 				self.b3.hide()
# 	def click5(self):
# 			self.b5.setText("1")
# 			if self.b5.text()==self.b1.text():
# 				self.b5.hide()
# 				self.b1.hide()
# 	def click6(self):
# 			self.b6.setText("3")
# 			if self.b6.text()==self.b2.text():
# 				self.b6.hide()
# 				self.b2.hide()

# window=Window()
# sys.exit(app.exec_())


# 3-MASALA

# from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QWidget,QFrame
# from PyQt5 import QtGui,QtCore
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# import sys

# app=QApplication(sys.argv)
# class Calc(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(500,150,420,490)
# 		self.setWindowTitle("Calculator")
# 		self.start()
# 		self.show()
# 	def start(self):
# 		self.label=QLabel("0",self)
# 		self.label.setGeometry(40,50,340,70)
# 		self.label.setFont(QFont("JetBrains Mono",18))
# 		self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
# 		self.label.setFrameShape(QFrame.Box)
# 		self.label.setFrameShadow(QFrame.Raised)
# 		self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
# 		self.label.setWordWrap(False)

# 		self.pushButton1=QPushButton("1",self)
# 		self.pushButton1.setGeometry(40,140,70,60)
# 		self.pushButton1.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# 		self.pushButton2=QPushButton("2",self)
# 		self.pushButton2.setGeometry(130,140,70,60)
# 		self.pushButton2.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# 		self.pushButton3=QPushButton("3",self)
# 		self.pushButton3.setGeometry(220,140,70,60)
# 		self.pushButton3.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton4=QPushButton("+",self)
# 		self.pushButton4.setGeometry(310,140,70,110)
# 		self.pushButton4.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton5=QPushButton("4",self)
# 		self.pushButton5.setGeometry(40,220,70,60)
# 		self.pushButton5.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton6=QPushButton("5",self)
# 		self.pushButton6.setGeometry(130,220,70,60)
# 		self.pushButton6.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton7=QPushButton("6",self)
# 		self.pushButton7.setGeometry(220,220,70,60)
# 		self.pushButton7.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton8=QPushButton("-",self)
# 		self.pushButton8.setGeometry(310,260,70,100)
# 		self.pushButton8.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton9=QPushButton("7",self)
# 		self.pushButton9.setGeometry(40,300,70,60)
# 		self.pushButton9.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton10=QPushButton("8",self)
# 		self.pushButton10.setGeometry(130,300,70,60)
# 		self.pushButton10.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton11=QPushButton("9",self)
# 		self.pushButton11.setGeometry(220,300,70,60)
# 		self.pushButton11.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.pushButton12=QPushButton("C",self)
# 		self.pushButton12.setGeometry(40,380,70,70)
# 		self.pushButton12.setFont(QFont("JetBrains Mono",13))
# 		self.pushButton12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		
# 		self.QPushButton13=QPushButton("=",self)
# 		self.QPushButton13.setGeometry(130,380,250,70)
# 		self.QPushButton13.setFont(QFont("JetBrains Mono",13))
# 		self.QPushButton13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# 		self.pushButton1.clicked.connect(self.bir)
# 		self.pushButton2.clicked.connect(self.ikki)
# 		self.pushButton3.clicked.connect(self.uch)
# 		self.pushButton4.clicked.connect(self.qosh)
# 		self.pushButton5.clicked.connect(self.tort)
# 		self.pushButton6.clicked.connect(self.besh)
# 		self.pushButton7.clicked.connect(self.olti)
# 		self.pushButton8.clicked.connect(self.ayir)
# 		self.pushButton9.clicked.connect(self.yetti)
# 		self.pushButton10.clicked.connect(self.sakkiz)
# 		self.pushButton11.clicked.connect(self.toqqiz)
# 		self.pushButton12.clicked.connect(self.c)
# 		self.QPushButton13.clicked.connect(self.hisobla)

# 	def bir(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"1"}')
# 	def ikki(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"2"}')
# 	def uch(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"3"}')
# 	def tort(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"4"}')
# 	def besh(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"5"}')
# 	def olti(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"6"}')
# 	def yetti(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"7"}')
# 	def sakkiz(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"8"}')
# 	def toqqiz(self):
# 		if self.label.text()=="0":
# 			self.label.setText("")
# 		self.label.setText(f'{self.label.text()}{"9"}')
# 	def c(self):
# 		self.label.setText("0")
# 	def qosh(self):
# 		self.label.setText(f'{self.label.text()}{"+"}')
# 	def ayir(self):
# 		self.label.setText(f'{self.label.text()}{"-"}')
# 	def teng(self):
# 		self.label.setText(f'{self.label.text()}'+f'{self.label.text()}')

# 	def hisobla(self):
# 		ifoda = self.label.text()
# 		if ifoda:
# 			ifoda = str(ifoda)
# 			natija = eval(ifoda)
# 			self.label.setText(str(natija))

# Calculator=Calc()
# sys.exit(app.exec_())