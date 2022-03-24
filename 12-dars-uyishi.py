import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtGui import QFont

dastur=QApplication(sys.argv)
oyna=QWidget()
oyna.setWindowTitle("Ma'lumot")
oyna.setGeometry(430,250,500,230)

btn1=QPushButton("familiya",oyna)
btn1.move(50,150)
btn1.setFont(QFont("JetBrains Mono",13))
btn2=QPushButton("ism",oyna)
btn2.move(200,150)
btn2.setFont(QFont("JetBrains Mono",13))

if btn2.clicked:
	def _ism_():
		ism=QLabel("Jo'rabek",oyna)
		ism.move(50,80)
		ism.setFont(QFont("JetBrains Mono",13)) 
		print(ism.show())
	btn2.clicked.connect(_ism_)

elif ( btn1.clicked and btn2.clicked):
	def _fam_():
		fam=QLabel("Boyxo'rozov",oyna)
		fam.move(50,80)
		fam.setFont(QFont("JetBrains Mono",13)) 
		print(fam.show())
		
	def _ism_():
		ism=QLabel("Jo'rabek",oyna)
		ism.move(200,80)
		ism.setFont(QFont("JetBrains Mono",13)) 
		print(ism.show())
	btn1.clicked.connect(_fam_)
	btn2.clicked.connect(_ism_)

oyna.show()
sys.exit(dastur.exec_())