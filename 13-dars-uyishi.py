# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QPushButton, QRadioButton,QLabel
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(400,200,500,370)
# 		self.setWindowTitle("Test")
# 		self.bir()
# 		self.show()
	
# 	def font(self,ob):
# 		ob.setFont(QFont("JetBrains Mono",13))
	
# 	def bir(self):
# 		self.savol1=QLabel("1 kun necha soatga teng?",self)
# 		self.font(self.savol1)
# 		self.savol1.move(50,50)
# 		self.a1=QRadioButton("13",self)
# 		self.font(self.a1)
# 		self.a1.move(50,100)
# 		self.a2=QRadioButton("24",self)
# 		self.font(self.a2)
# 		self.a2.move(50,150)
# 		self.a3=QRadioButton("23",self)
# 		self.font(self.a3)
# 		self.a3.move(50,200)
# 		self.a4=QRadioButton("31",self)
# 		self.font(self.a4)
# 		self.a4.move(50,250)
		
# 		self.next=QPushButton("Keyingi",self)
# 		self.font(self.next)
# 		self.next.move(350,290)
		
# 		self.next.clicked.connect(self.ikki)

# 	def ikki(self):
# 		self.savol2=QLabel("1 soat necha daqiqaga teng?",self)
# 		self.font(self.savol2)
# 		self.savol2.move(50,50)
# 		self.a5=QRadioButton("100",self)
# 		self.font(self.a5)
# 		self.a5.move(50,100)
# 		self.a6=QRadioButton("60",self)
# 		self.font(self.a6)
# 		self.a6.move(50,150)
# 		self.a7=QRadioButton("180",self)
# 		self.font(self.a7)
# 		self.a7.move(50,200)
# 		self.a8=QRadioButton("80",self)
# 		self.font(self.a8)
# 		self.a8.move(50,250)

# 		self.next1=QPushButton("Keyingi",self)
# 		self.font(self.next1)
# 		self.next1.move(350,290)

# 		self.savol1.hide()
# 		self.a1.hide()
# 		self.a2.hide()
# 		self.a3.hide()
# 		self.a4.hide()
# 		self.next.hide()
# 		self.savol2.adjustSize()
# 		self.savol2.show()
# 		self.a5.show()
# 		self.a6.show()
# 		self.a7.show()
# 		self.a8.show()
# 		self.next1.show()

# 		self.next1.clicked.connect(self.uch)

# 	def uch(self):
# 		self.savol3=QLabel("1 daqiqa necha sekundga teng?",self)
# 		self.font(self.savol3)
# 		self.savol3.move(50,50)
# 		self.a9=QRadioButton("100",self)
# 		self.font(self.a9)
# 		self.a9.move(50,100)
# 		self.a10=QRadioButton("80",self)
# 		self.font(self.a10)
# 		self.a10.move(50,150)
# 		self.a11=QRadioButton("3600",self)
# 		self.font(self.a11)
# 		self.a11.move(50,200)
# 		self.a12=QRadioButton("60",self)
# 		self.font(self.a12)
# 		self.a12.move(50,250)

# 		self.next2=QPushButton("Keyingi",self)
# 		self.font(self.next2)
# 		self.next2.move(350,290)

# 		self.savol2.hide()
# 		self.a5.hide()
# 		self.a6.hide()
# 		self.a7.hide()
# 		self.a8.hide()
# 		self.next1.hide()
# 		self.savol3.adjustSize()
# 		self.savol3.show()
# 		self.a9.show()
# 		self.a10.show()
# 		self.a11.show()
# 		self.a12.show()
# 		self.next2.show()
		
# 		self.next2.clicked.connect(self.tort)

# 	def tort(self):
# 		self.savol4=QLabel("1 hafta necha kunga teng?",self)
# 		self.font(self.savol4)
# 		self.savol4.move(50,50)
# 		self.a13=QRadioButton("7",self)
# 		self.font(self.a13)
# 		self.a13.move(50,100)
# 		self.a14=QRadioButton("14",self)
# 		self.font(self.a14)
# 		self.a14.move(50,150)
# 		self.a15=QRadioButton("5",self)
# 		self.font(self.a15)
# 		self.a15.move(50,200)
# 		self.a16=QRadioButton("10",self)
# 		self.font(self.a16)
# 		self.a16.move(50,250)

# 		self.next3=QPushButton("Keyingi",self)
# 		self.font(self.next3)
# 		self.next3.move(350,290)

# 		self.savol3.hide()
# 		self.a9.hide()
# 		self.a10.hide()
# 		self.a11.hide()
# 		self.a12.hide()
# 		self.next2.hide()
# 		self.savol4.adjustSize()
# 		self.savol4.show()
# 		self.a13.show()
# 		self.a14.show()
# 		self.a15.show()
# 		self.a16.show()
# 		self.next3.show()

# 		self.next3.clicked.connect(self.besh)

# 	def besh(self):
# 		self.savol5=QLabel("1 yil necha oyga teng?",self)
# 		self.font(self.savol5)
# 		self.savol5.move(50,50)
# 		self.a17=QRadioButton("24",self)
# 		self.font(self.a17)
# 		self.a17.move(50,100)
# 		self.a18=QRadioButton("12",self)
# 		self.font(self.a18)
# 		self.a18.move(50,150)
# 		self.a19=QRadioButton("13",self)
# 		self.font(self.a19)
# 		self.a19.move(50,200)
# 		self.a20=QRadioButton("10",self)
# 		self.font(self.a20)
# 		self.a20.move(50,250)

# 		self.next4=QPushButton("Natija",self)
# 		self.font(self.next4)
# 		self.next4.move(350,290)

# 		self.savol4.hide()
# 		self.a13.hide()
# 		self.a14.hide()
# 		self.a15.hide()
# 		self.a16.hide()
# 		self.next3.hide()
# 		self.savol5.adjustSize()
# 		self.savol5.show()
# 		self.a17.show()
# 		self.a18.show()
# 		self.a19.show()
# 		self.a20.show()
# 		self.next4.show()

# 		self.next4.clicked.connect(self.natija)

# 	def natija(self):
# 		j=0
# 		if self.a2.isChecked():
# 			j+=1
# 		if self.a6.isChecked():
# 			j+=1
# 		if self.a12.isChecked():
# 			j+=1
# 		if self.a13.isChecked():
# 			j+=1
# 		if self.a18.isChecked():
# 			j+=1

# 		self.savol5.hide()
# 		self.a17.hide()
# 		self.a18.hide()
# 		self.a19.hide()
# 		self.a20.hide()
# 		self.next4.hide()
# 		self.b=QLabel("{} ta to'g'ri javob topdingiz".format(j),self)
# 		self.font(self.b)
# 		self.b.move(50,50)
# 		self.b.show()
		
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
# 		self.setGeometry(400,200,500,600)
# 		self.setWindowTitle("Milliy Taomlar")
# 		self.bir()
# 		self.show()
	
# 	def font(self,ob):
# 		ob.setFont(QFont("JetBrains Mono",13))
	
# 	def bir(self):
# 		self.savol1=QLabel("1 - Taomlar ro'yxati",self)
# 		self.font(self.savol1)
# 		self.savol1.move(50,50)
# 		self.a1=QCheckBox("Somsa - 10000",self)
# 		self.font(self.a1)
# 		self.a1.move(50,100)
# 		self.a2=QCheckBox("Mastava - 20000",self)
# 		self.font(self.a2)
# 		self.a2.move(50,150)
# 		self.a3=QCheckBox("Moshxo'rda - 25000",self)
# 		self.font(self.a3)
# 		self.a3.move(50,200)
# 		self.a4=QCheckBox("Manti - 30000",self)
# 		self.font(self.a4)
# 		self.a4.move(50,250)
# 		self.a5=QCheckBox("Osh - 35000",self)
# 		self.font(self.a5)
# 		self.a5.move(50,300)		
		
# 		self.next=QPushButton("2 - Taomlar",self)
# 		self.font(self.next)
# 		self.next.move(350,290)
		
# 		self.next.clicked.connect(self.ikki)

# 	def ikki(self):
# 		self.savol2=QLabel("2 - Taomlar ro'yxati",self)
# 		self.font(self.savol2)
# 		self.savol2.move(50,50)
# 		self.a6=QCheckBox("Dimlama - 30000",self)
# 		self.font(self.a6)
# 		self.a6.move(50,100)
# 		self.a7=QCheckBox("Qovurma - 25000",self)
# 		self.font(self.a7)
# 		self.a7.move(50,150)
# 		self.a8=QCheckBox("Chuchvara - 15000",self)
# 		self.font(self.a8)
# 		self.a8.move(50,200)
# 		self.a9=QCheckBox("Norin - 18000",self)
# 		self.font(self.a9)
# 		self.a9.move(50,250)
# 		self.a10=QCheckBox("Do'lma - 19000",self)
# 		self.font(self.a10)
# 		self.a10.move(50,300)

# 		self.next1=QPushButton("Ichimliklar",self)
# 		self.font(self.next1)
# 		self.next1.move(350,290)

# 		self.savol1.hide()
# 		self.a1.hide()
# 		self.a2.hide()
# 		self.a3.hide()
# 		self.a4.hide()
# 		self.a5.hide()
# 		self.next.hide()
# 		self.savol2.adjustSize()
# 		self.savol2.show()
# 		self.a6.show()
# 		self.a7.show()
# 		self.a8.show()
# 		self.a9.show()
# 		self.a10.show()
# 		self.next1.show()

# 		self.next1.clicked.connect(self.uch)

# 	def uch(self):
# 		self.savol3=QLabel("Ichimliklar ro'yxati",self)
# 		self.font(self.savol3)
# 		self.savol3.move(50,50)
# 		self.a11=QCheckBox("Sharbat - 8000",self)
# 		self.font(self.a11)
# 		self.a11.move(50,100)
# 		self.a12=QCheckBox("Choy - 5000",self)
# 		self.font(self.a12)
# 		self.a12.move(50,150)
# 		self.a13=QCheckBox("Pepsi - 9000",self)
# 		self.font(self.a13)
# 		self.a13.move(50,200)
# 		self.a14=QCheckBox("Coca-Cola - 10000",self)
# 		self.font(self.a14)
# 		self.a14.move(50,250)
# 		self.a15=QCheckBox("RC Cola - 7000",self)
# 		self.font(self.a15)
# 		self.a15.move(50,300)
# 		self.next2=QPushButton("Desertlar",self)
# 		self.font(self.next2)
# 		self.next2.move(350,290)

# 		self.savol2.hide()
# 		self.a6.hide()
# 		self.a7.hide()
# 		self.a8.hide()
# 		self.a9.hide()
# 		self.a10.hide()
# 		self.next1.hide()
# 		self.savol3.adjustSize()
# 		self.savol3.show()
# 		self.a11.show()
# 		self.a12.show()
# 		self.a13.show()
# 		self.a14.show()
# 		self.a15.show()
# 		self.next2.show()
		
# 		self.next2.clicked.connect(self.tort)

# 	def tort(self):
# 		self.savol4=QLabel("Desertlar ro'yxati",self)
# 		self.font(self.savol4)
# 		self.savol4.move(50,50)
# 		self.a16=QCheckBox("Kruassan - 15000",self)
# 		self.font(self.a16)
# 		self.a16.move(50,100)
# 		self.a17=QCheckBox("Vafli - 8000",self)
# 		self.font(self.a17)
# 		self.a17.move(50,150)
# 		self.a18=QCheckBox("Chizkeyk - 13000",self)
# 		self.font(self.a18)
# 		self.a18.move(50,200)
# 		self.a19=QCheckBox("Shokolatli - 15000",self)
# 		self.font(self.a19)
# 		self.a19.move(50,250)
# 		self.a20=QCheckBox("Dietali - 9000",self)
# 		self.font(self.a20)
# 		self.a20.move(50,300)

# 		self.next3=QPushButton("Hisob",self)
# 		self.font(self.next3)
# 		self.next3.move(350,290)

# 		self.savol3.hide()
# 		self.a11.hide()
# 		self.a12.hide()
# 		self.a13.hide()
# 		self.a14.hide()
# 		self.a15.hide()
# 		self.next2.hide()
# 		self.savol4.adjustSize()
# 		self.savol4.show()
# 		self.a16.show()
# 		self.a17.show()
# 		self.a18.show()
# 		self.a19.show()
# 		self.a20.show()
# 		self.next3.show()

# 		self.next3.clicked.connect(self.natija)
# 		self.next3.clicked.connect(self.natija1)
# 		self.next3.clicked.connect(self.natija2)
# 		self.next3.clicked.connect(self.natija3)

# 	def natija(self):
# 		self.a16.hide()
# 		self.a17.hide()
# 		self.a18.hide()
# 		self.a19.hide()
# 		self.a20.hide()
# 		self.next3.hide()


# 		self.royxat=QLabel("Siz xarid qildingiz:",self)
# 		self.font(self.royxat)
# 		self.royxat.move(150,10)
# 		self.royxat.show()
# 		self.savol1.setText("1 - Taomlardan:\n")
# 		if self.a1.isChecked():
# 			self.savol1.setText(self.savol1.text()+self.a1.text()+"\n")
# 		if self.a2.isChecked():
# 			self.savol1.setText(self.savol1.text()+self.a2.text()+"\n")
# 		if self.a3.isChecked():
# 			self.savol1.setText(self.savol1.text()+self.a3.text()+"\n")
# 		if self.a4.isChecked():
# 			self.savol1.setText(self.savol1.text()+self.a4.text()+"\n")
# 		if self.a5.isChecked():
# 			self.savol1.setText(self.savol1.text()+self.a5.text()+"\n")
# 		self.savol1.move(50,50)
# 		self.savol1.show()
		
# 	def natija1(self):
		
# 		self.a16.hide()
# 		self.a17.hide()
# 		self.a18.hide()
# 		self.a19.hide()
# 		self.a20.hide()
# 		self.next3.hide()
# 		self.savol2.setText("2 - Taomlardan:\n")
# 		if self.a6.isChecked():
# 			self.savol2.setText(self.savol2.text()+self.a6.text()+"\n")
# 		if self.a7.isChecked():
# 			self.savol2.setText(self.savol2.text()+self.a7.text()+"\n")
# 		if self.a8.isChecked():
# 			self.savol2.setText(self.savol2.text()+self.a8.text()+"\n")
# 		if self.a9.isChecked():
# 			self.savol2.setText(self.savol2.text()+self.a9.text()+"\n")
# 		if self.a10.isChecked():
# 			self.savol2.setText(self.savol2.text()+self.a10.text()+"\n")
# 		self.savol2.move(50,180)
# 		self.savol2.show()
	
# 	def natija2(self):
		
# 		self.a16.hide()
# 		self.a17.hide()
# 		self.a18.hide()
# 		self.a19.hide()
# 		self.a20.hide()
# 		self.next3.hide()
# 		self.savol3.setText("Ichimliklardan:\n")
# 		if self.a11.isChecked():
# 			self.savol3.setText(self.savol3.text()+self.a11.text()+"\n")
# 		if self.a12.isChecked():
# 			self.savol3.setText(self.savol3.text()+self.a12.text()+"\n")
# 		if self.a13.isChecked():
# 			self.savol3.setText(self.savol3.text()+self.a13.text()+"\n")
# 		if self.a14.isChecked():
# 			self.savol3.setText(self.savol3.text()+self.a14.text()+"\n")
# 		if self.a15.isChecked():
# 			self.savol3.setText(self.savol3.text()+self.a15.text()+"\n")
# 		self.savol3.move(50,310)
# 		self.savol3.show()

# 	def natija3(self):
		
# 		self.a16.hide()
# 		self.a17.hide()
# 		self.a18.hide()
# 		self.a19.hide()
# 		self.a20.hide()
# 		self.next3.hide()
# 		self.savol4.setText("Desertlardan:\n")
# 		if self.a16.isChecked():
# 			self.savol4.setText(self.savol4.text()+self.a16.text()+"\n")
# 		if self.a17.isChecked():
# 			self.savol4.setText(self.savol4.text()+self.a17.text()+"\n")
# 		if self.a18.isChecked():
# 			self.savol4.setText(self.savol4.text()+self.a18.text()+"\n")
# 		if self.a19.isChecked():
# 			self.savol4.setText(self.savol4.text()+self.a19.text()+"\n")
# 		if self.a20.isChecked():
# 			self.savol4.setText(self.savol4.text()+self.a20.text()+"\n")	
# 		self.savol4.move(50,440)
# 		self.savol4.show()

# oyna=Window()
# sys.exit(app.exec_())



# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QPushButton, QComboBox,QLabel
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setGeometry(250,150,550,500)
# 		self.setWindowTitle("Ma'lumot")
# 		self.start()
# 		self.show()
# 	def font(self,ob):
# 		ob.setFont(QFont("JetBrains Mono",13))
# 	def start(self):
# 		self.info=QLabel("Ma'lumotlaringizni tanlang",self)
# 		self.font(self.info)
# 		self.info.move(140,50)
# 		self.joy=QComboBox(self)
# 		self.font(self.joy)
# 		self.joy.move(40,150)
# 		self.joy.addItems(["Toshkent","Samarqand","Jizzax","Andijon","Buxoro","Farg'ona","Namangan","Qoraqalpog'iston","Navoiy","Sirdaryo","Xorazm","Qashqadaryo","Surxondaryo"])
# 		self.jins=QComboBox(self)
# 		self.font(self.jins)
# 		self.jins.move(280,150)
# 		self.jins.addItems(["Erkak","Ayol"])
# 		self.millat=QComboBox(self)
# 		self.font(self.millat)
# 		self.millat.move(410,150)
# 		self.millat.addItems(["O'zbek","Rus","Ingliz","Turk","Qozoq"])
# 		self.up=QPushButton("Tayyor",self)
# 		self.font(self.up)
# 		self.up.move(230,250)
# 		self.up.clicked.connect(self.run)
# 		self.bir=QLabel("",self)
# 		self.font(self.bir)
# 		self.bir.move(40,330)
# 		self.ikki=QLabel("",self)
# 		self.font(self.ikki)
# 		self.ikki.move(40,380)
# 		self.uch=QLabel("",self)
# 		self.font(self.uch)
# 		self.uch.move(40,430)
# 	def run(self):
# 		self.bir.setText("Viloyati: "+self.joy.currentText())
# 		self.bir.adjustSize()
# 		self.ikki.setText("Jinsi: "+self.jins.currentText())
# 		self.ikki.adjustSize()
# 		self.uch.setText("Millati: "+self.millat.currentText())
# 		self.uch.adjustSize()
		
# info=Window()
# sys.exit(app.exec_())