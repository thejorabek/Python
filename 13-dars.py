# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(200,200,500,200)
# 		self.setWindowTitle("Horizontal and Vertical box layout")
# 		self.start()
# 		self.show()
# 	def font(self,ob):
# 		ob.setFont(QFont("JetBrains Mono",13))
# 	def start(self):
# 		ok=QPushButton("OK",self)
# 		self.font(ok)
# 		cancel=QPushButton("CANCEL",self)
# 		self.font(cancel)
# 		# hbox=QHBoxLayout(self)
# 		# hbox.addStretch()
# 		# hbox.addWidget(ok)
# 		# hbox.addStretch()
# 		# hbox.addWidget(cancel)
# 		# hbox.addStretch()
		
# 		vbox=QVBoxLayout(self)
# 		vbox.addStretch()
# 		vbox.addWidget(ok)  
# 		vbox.addStretch()
# 		vbox.addWidget(cancel)
# 		vbox.addStretch()
# oyna=Window()
# sys.exit(app.exec_())

# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QPushButton, QCheckBox,QLabel
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(200,200,600,500)
# 		self.setWindowTitle("QCheckBox")
# 		self.start()
# 		self.show()
# 	def font(self,ob):
# 		ob.setFont(QFont("JetBrains Mono",20))
# 	def start(self):
# 		self.yozuv=QLabel("Nimadir",self)
# 		self.font(self.yozuv)
# 		self.yozuv.move(50,50)
# 		self.a1=QCheckBox("aaaa",self)
# 		self.font(self.a1)
# 		self.a1.move(50,100)
# 		self.a2=QCheckBox("aaaa",self)
# 		self.font(self.a2)
# 		self.a2.move(50,150)
# 		self.a3=QCheckBox("aaaa",self)
# 		self.font(self.a3)
# 		self.a3.move(50,200)
# 		self.a4=QCheckBox("aaaa",self)
# 		self.font(self.a4)
# 		self.a4.move(50,250)
# 		self.tasdiq=QPushButton("Tasdiqlash",self)
# 		self.font(self.tasdiq)
# 		self.tasdiq.move(100,300)
# 		self.tasdiq.clicked.connect(self.result)
# 		self.back=QPushButton("<--",self)
# 		self.font(self.back)
# 		self.back.hide()
# 		self.back.clicked.connect(self.BACK)
# 	def BACK(self):
# 		self.yozuv.setText("Nimadir")
# 		self.yozuv.adjustSize()
# 		self.a1.show()
# 		self.a2.show()
# 		self.a3.show()
# 		self.a4.show()
# 		self.tasdiq.show()
# 		self.back.hide()
# 	def result(self):
# 		self.yozuv.setText("Sizning natijangiz:\n")
# 		if self.a1.isChecked():
# 			self.yozuv.setText(self.yozuv.text()+self.a1.text()+"\n")
# 		if self.a2.isChecked():
# 			self.yozuv.setText(self.yozuv.text()+self.a2.text()+"\n")
# 		if self.a3.isChecked():
# 			self.yozuv.setText(self.yozuv.text()+self.a3.text()+"\n")
# 		if self.a4.isChecked():
# 			self.yozuv.setText(self.yozuv.text()+self.a4.text()+"\n")
# 		self.yozuv.adjustSize()
# 		self.a1.hide()
# 		self.a2.hide()
# 		self.a3.hide()
# 		self.a4.hide()
# 		self.tasdiq.hide()
# 		self.back.show()
# oyna=Window()
# sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QComboBox,QLabel
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(250,150,550,500)
		self.setWindowTitle("Ma'lumot")
		self.start()
		self.show()
	def font(self,ob):
		ob.setFont(QFont("JetBrains Mono",13))
	def start(self):
		info=QLabel("Ma'lumotlaringizni tanlang",self)
		self.font(info)
		info.move(140,50)
		self.joy=QComboBox(self)
		self.font(self.joy)
		self.joy.move(40,150)
		self.joy.addItems(["Toshkent","Samarqand","Jizzax","Andijon","Buxoro","Farg'ona","Namangan","Qoraqalpog'iston","Navoiy","Sirdaryo","Xorazm","Qashqadaryo","Surxondaryo"])
		self.jins=QComboBox(self)
		self.font(self.jins)
		self.jins.move(280,150)
		self.jins.addItems(["Erkak","Ayol"])
		self.millat=QComboBox(self)
		self.font(self.millat)
		self.millat.move(410,150)
		self.millat.addItems(["O'zbek","Rus","Ingliz","Turk","Qozoq"])
		up=QPushButton("Tayyor",self)
		self.font(up)
		up.move(230,250)
		up.clicked.connect(self.run)
		self.bir=QLabel("",self)
		self.font(self.bir)
		self.bir.move(40,330)
		self.ikki=QLabel("",self)
		self.font(self.ikki)
		self.ikki.move(40,380)
		self.uch=QLabel("",self)
		self.font(self.uch)
		self.uch.move(40,430)
		

	def run(self):
		self.bir.setText("Viloyati: "+self.joy.currentText())
		self.bir.adjustSize()
		self.ikki.setText("Jinsi: "+self.jins.currentText())
		self.ikki.adjustSize()
		self.uch.setText("Millati: "+self.millat.currentText())
		self.uch.adjustSize()
		
info=Window()
sys.exit(app.exec_())