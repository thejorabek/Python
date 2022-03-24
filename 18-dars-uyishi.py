from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QComboBox,QMessageBox
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QFont
from PyQt5 import QtGui,QtCore
import sys,sqlite3
class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("Chat.db")
        self.kur=self.con.cursor()
        self.create()
        self.setGeometry(400, 250, 500, 300)
        self.btn=QPushButton("Login",self)
        self.btn.setFont(QFont("JetBrains Mono",13))
        self.btn.move(370, 230)
        self.second=SecondWindow()
        self.login=QLineEdit(self)
        self.login.setGeometry(150,50,300,40)
        self.font(self.login)
        self.login.setMaxLength(18)
        self.login.setPlaceholderText("Loginni kiriting...")
        self.parol=QLineEdit(self)
        self.parol.setGeometry(150,150,300,40)
        self.font(self.parol)
        self.parol.setMaxLength(10)
        self.parol.setPlaceholderText("Parolni kiriting...")
        self.parol.setEchoMode(QLineEdit.Password)
        self.label_l=QLabel("Login",self)
        self.label_l.move(40,55)
        self.label_l.setFont(QFont("JetBrains Mono",15))
        self.label_l.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_p=QLabel("Parol",self)
        self.label_p.move(40,155)
        self.label_p.setFont(QFont("JetBrains Mono",15))
        self.label_p.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.btn.clicked.connect(self.run1)

        lst=[("admin","12345",""),("user","54321","")]

    def create(self):
    	self.kur.execute("CREATE TABLE IF NOT EXISTS whatsapp(login TEXT, parol TEXT, chat TEXT)")
    	self.con.commit()
    
    def font(self,ob):
        ob.setFont(QFont("JetBrains Mono",13))

    def run1(self):
        if self.login.text()=="" or self.parol.text()=="":
            win=QMessageBox(self)
            self.font(win)
            win.setText("Ma'lumotlar to'ldirilmagan")
            win.show()
        else:
            self.second.show()
            self.hide()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 200, 600, 400)
        self.line=QLineEdit(self)
        self.line.setGeometry(30,30,260,170)
        self.line.setFont(QFont("JetBrains Mono",13))
        self.line.setPlaceholderText("Yozing...")
        self.linee=QLineEdit(self)
        self.linee.setGeometry(300,30,270,170)
        self.linee.setFont(QFont("JetBrains Mono",13))
        self.linee.setReadOnly(True)
        self.combo=QComboBox(self)
        self.combo.setGeometry(250,230,100,40)
        self.combo.addItems(["Admin","User"])
        self.send=QPushButton("Send",self)
        self.send.setGeometry(250,280,100,40)
        self.btn=QPushButton("Ortga",self)
        self.btn.clicked.connect(self.run)
        self.btn.setGeometry(250,330,100,40)
        self.labell=QLabel("Qabul qiluvchini tanlang ->",self)
        self.labell.move(30,240)
        self.labell.setFont(QFont("JetBrains Mono",10))
        self.send.clicked.connect(self.sendd)

        self.insert()
    def sendd(self):
        self.linee.setText(self.linee.text()+"\n"+self.line.text())
        self.line.clear()

    def insert(self,c):
        self.kur.execute("INSERT INTO whatsapp VALUES(?)",self.linee.text())
        self.insert(c)
        self.con.commit()
        
    def run(self):
        self.qqq=FirstWindow()
        self.qqq.show()
        self.hide()
app=QApplication(sys.argv)
oyna=FirstWindow()
oyna.show()
sys.exit(app.exec_())
oyna.con.close()