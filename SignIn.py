from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QPushButton,QWidget,QVBoxLayout,QCheckBox,QComboBox,QRadioButton
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import QFont
import sys,sqlite3

app=QApplication(sys.argv)
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(500,250,400,300)
		self.setWindowTitle("Facebook")
		self.start()
		self.show()
	def font(self,ob):
		ob.setFont(QFont("JetBrains Mono",13))
	def start(self):
		self.label=QLabel("Log Into Facebook",self)
		self.label.move(110,10)
		self.font(self.label)
		self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

		self.email=QLineEdit(self)
		self.email.setGeometry(50,50,300,50)
		self.font(self.email)
		self.email.setMaxLength(18)
		self.email.setPlaceholderText("Email or Phone number")

		self.password=QLineEdit(self)
		self.password.setGeometry(50,120,300,50)
		self.font(self.password)
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaxLength(13)
		self.password.setPlaceholderText("Password")

		self.login=QPushButton("Log In",self)
		self.login.setGeometry(50,190,300,40)
		self.font(self.login)
		self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.login.setStyleSheet("background-color : rgb(11,87,187)")

		self.forgot=QPushButton("Forgot your password?",self)
		self.forgot.setGeometry(35,250,165,30)
		self.forgot.setFont(QFont("JetBrains Mono",9))
		self.forgot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.signUp=QPushButton("Sign Up for Facebook",self)
		self.signUp.setGeometry(220,250,160,30)
		self.signUp.setFont(QFont("JetBrains Mono",9))
		self.signUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.signUp.clicked.connect(self.sign)
		self.forgot.clicked.connect(self._forgot)

	def sign(self):
		self.signw=SignUp()
		self.signw.show()
		self.close()
	def _forgot(self):
		self._f_=Forgot()
		self._f_.show()
		self.close()

class SignUp(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(500,150,410,520)
		self.setWindowTitle("Facebook")
		self.start()
		self.show()
	def start(self):
		self.label1=QLabel("Create a new account",self)
		self.label1.setFont(QFont("JetBrains Mono",14))
		self.label1.setGeometry(80,10,230,20)
		self.label1.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.label2=QLabel("It's quick and easy",self)
		self.label2.setGeometry(115,40,150,20)
		self.label2.setFont(QFont("JetBrains Mono",10))
		self.label2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.lineEdit=QLineEdit(self)
		self.lineEdit.setGeometry(27,90,160,30)
		self.lineEdit.setFont(QFont("JetBrains Mono",13))
		self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.lineEdit.setPlaceholderText("First name")
		self.lineEdit.setMaxLength(15)
		
		self.lineEdit1=QLineEdit(self)
		self.lineEdit1.setGeometry(215,90,170,30)
		self.lineEdit1.setFont(QFont("JetBrains Mono",13))
		self.lineEdit1.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.lineEdit1.setPlaceholderText("Second name")
		self.lineEdit1.setMaxLength(15)
		
		self.lineEdit2=QLineEdit(self)
		self.lineEdit2.setGeometry(27,140,358,30)
		self.lineEdit2.setFont(QFont("JetBrains Mono",13))
		self.lineEdit2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.lineEdit2.setPlaceholderText("Mobile number or email")
		self.lineEdit2.setMaxLength(30)
		
		self.lineEdit3=QLineEdit(self)
		self.lineEdit3.setGeometry(27,190,358,30)
		self.lineEdit3.setFont(QFont("JetBrains Mono",13))
		self.lineEdit3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.lineEdit3.setPlaceholderText("New password")
		self.lineEdit3.setEchoMode(QLineEdit.Password)
		self.lineEdit3.setMaxLength(20)
		
		self.checkBox=QCheckBox("Save password",self)
		self.checkBox.setGeometry(260,230,130,25)
		self.checkBox.setChecked(1)
		
		self.label2=QLabel("Birthday",self)
		self.label2.setFont(QFont("JetBrains Mono",9))
		self.label2.setGeometry(27,245,65,20)
		self.label2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.comboBox=QComboBox(self)
		self.comboBox.addItems(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
		self.comboBox.setGeometry(27,270,110,27)
		
		self.comboBox1=QComboBox(self)
		self.comboBox1.addItems(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
		self.comboBox1.setGeometry(160,270,100,27)
		
		self.comboBox3=QComboBox(self)
		self.comboBox3.addItems(["2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990"])
		self.comboBox3.setGeometry(280,270,100,27)
		
		self.label3=QLabel("Gender",self)
		self.label3.setFont(QFont("JetBrains Mono",9))
		self.label3.setGeometry(27,305,65,20)
		self.label3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.lineEdit4=QLineEdit(self)
		self.lineEdit4.setGeometry(27,330,110,25)
		self.lineEdit4.setFont(QFont("JetBrains Mono",13))
		self.lineEdit4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.radioButton=QRadioButton("Female",self)
		self.radioButton.setGeometry(35,330,110,25)
		
		self.lineEdit5=QLineEdit(self)
		self.lineEdit5.setGeometry(160,330,100,25)
		self.lineEdit5.setFont(QFont("JetBrains Mono",13))
		self.lineEdit5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.radioButton1=QRadioButton("Male",self)
		self.radioButton1.setGeometry(168,330,110,25)
		
		self.lineEdit6=QLineEdit(self)
		self.lineEdit6.setGeometry(280,330,100,25)
		self.lineEdit6.setFont(QFont("JetBrains Mono",13))
		self.lineEdit6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		
		self.radioButton2=QRadioButton("Custom",self)
		self.radioButton2.setGeometry(288,330,110,25)

		self.label4=QLabel("By clicking Sign Up, you agree to our Terms, Data Policy\nand Cookies Policy. You may receive SMS Notifications\n            from us and can upt out any time",self)
		self.label4.setFont(QFont("JetBrains Mono",8))
		self.label4.setGeometry(27,370,370,40)

		self.pushButton=QPushButton("Sign Up",self)
		self.pushButton.setGeometry(120,425,150,40)
		self.pushButton.setFont(QFont("JetBrains Mono",13))
		self.pushButton.setStyleSheet("background-color : rgb(11,87,187)")
		self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.label5=QPushButton("Already have an account?",self)
		self.label5.setGeometry(115,480,175,30)
		self.setFont(QFont("JetBrains Mono",9))
		self.label5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.label5.clicked.connect(self._login)

	def _login(self):
		self._login=Window()
		self._login.show()
		self.hide()

class Forgot(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(450,250,590,300)
		self.setWindowTitle("Facebook")
		self.start()
		self.show()
	def start(self):
		self.feed=QLabel("Find Your Account",self)
		self.feed.setGeometry(30,10,400,50)
		self.feed.setFont(QFont("JetBrains Mono",17))

		self.feef_=QLabel("Please enter your email or mobile number to search for your\naccount.",self)
		self.feef_.setGeometry(30,70,550,50)
		self.feef_.setFont(QFont("JetBrains Mono",11))

		self.f_forgot=QLineEdit(self)
		self.f_forgot.setGeometry(30,150,530,40)
		self.f_forgot.setFont(QFont("JetBrains Mono",13))
		self.f_forgot.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.f_forgot.setPlaceholderText("Email or mobile number")
		self.f_forgot.setMaxLength(30)

		self.cancel=QPushButton("Cancel",self)
		self.cancel.setGeometry(335,225,100,40)
		self.cancel.setFont(QFont("JetBrains Mono",13))
		self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.search=QPushButton("Search",self)
		self.search.setGeometry(460,225,100,40)
		self.search.setFont(QFont("JetBrains Mono",13))
		self.search.setStyleSheet("background-color : rgb(11,87,187)")
		self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.cancel.clicked.connect(self._cancel)

	def _cancel(self):
		self._login_=Window()
		self._login_.show()
		self.hide()

Facebook=Window()
sys.exit(app.exec_())