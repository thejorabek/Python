from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QRadioButton
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QFont
import sys,sqlite3
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("STUDENT.db")
        self.kur=self.con.cursor()
        self.setGeometry(200,200,1200,800)
        self.setWindowTitle("DATABASE AND PYQT5")
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",30))
        ob.move(x,y)
    def start(self):
        self.create()
        self.y1=QLabel("ID:",self)
        self.font(self.y1,50,50)
        self.y2=QLabel("NAME:",self)
        self.font(self.y2,50,120)
        self.y3=QLabel("SCORE:",self)
        self.font(self.y3,50,190)
        self.l1=QLineEdit(self)
        self.font(self.l1,250,50)
        self.l1.setPlaceholderText("idni kiriting.....")
        self.l2=QLineEdit(self)
        self.font(self.l2,250,120)
        self.l2.setPlaceholderText("nomini kiriting.....")
        self.l3=QLineEdit(self)
        self.font(self.l3,250,190)
        self.l3.setPlaceholderText("bahoni kiriting.....")
        self.v1=QRadioButton("Id",self)
        self.font(self.v1,650,50)
        self.v2=QRadioButton("Name",self)
        self.font(self.v2,650,120)
        self.v3=QRadioButton("Score",self)
        self.font(self.v3,650,190)
        self.matn=QLineEdit(self)
        self.font(self.matn,650,260)
        self.add=QPushButton("ADD",self)
        self.font(self.add,50,260)
        self.add.clicked.connect(self.ADD)
        self.delete=QPushButton("DELETE",self)
        self.font(self.delete,180,260)
        self.delete.clicked.connect(self.DELETE)
        self.update=QPushButton("UPDATE",self)
        self.font(self.update,650,330)
        self.update.clicked.connect(self.UPDATE)
        self.search=QPushButton("SEARCH",self)
        self.font(self.search,850,330)
        self.search.clicked.connect(self.SEARCH)
        self.table=QTableWidget(3,3,self)
        self.table.setFont(QFont("Times",20))
        self.table.setGeometry(50,400,450,150)
        self.table.setHorizontalHeaderLabels(['id','name','score'])
    def ADD(self):
        if self.l1.text()!="" and self.l2.text()!="" and self.l3.text()!="":
            a=int(self.l1.text())
            b=self.l2.text()
            c=int(self.l3.text())
            self.insert(a,b,c)
            self.l1.clear()
            self.l2.clear()
            self.l3.clear()
        else:
            win=QMessageBox(self)
            self.font(win,0,0)
            win.setText("Ma'lumotlar to'ldirilmagan")
            win.show()
    def DELETE(self):
        if self.l1.text()!="" and self.l2.text()!="" and self.l3.text()!="":
            a=int(self.l1.text())
            b=self.l2.text()
            c=int(self.l3.text())
            self.kur.execute("DELETE FROM talaba WHERE id=? AND name=? AND score=?",(a,b,c))
            self.con.commit()
            self.l1.clear()
            self.l2.clear()
            self.l3.clear()
        else:
            win=QMessageBox(self)
            self.font(win,0,0)
            win.setText("Ma'lumotlar to'ldirilmagan")
            win.show()
    def UPDATE(self):
        if self.l1.text()!="" and self.l2.text()!="" and self.l3.text()!="":
            a=int(self.l1.text())
            b=self.l2.text()
            c=int(self.l3.text())
            if self.v1.isChecked():
                d=int(self.matn.text())
                self.kur.execute("UPDATE talaba SET id=?, name=?, score=? WHERE id=?",(a,b,c,d))
            elif self.v2.isChecked():
                d=self.matn.text()
                self.kur.execute("UPDATE talaba SET id=?, name=?, score=? WHERE name=?",(a,b,c,d))
            elif self.v3.isChecked():
                d=int(self.matn.text())
                self.kur.execute("UPDATE talaba SET id=?, name=?, score=? WHERE score=?",(a,b,c,d))
            self.con.commit()
            self.l1.clear()
            self.l2.clear()
            self.l3.clear()
            self.matn.clear()
    def SEARCH(self):
        if self.v1.isChecked():
            text=int(self.matn.text())
            self.kur.execute("SELECT * FROM talaba WHERE id=?",(text,))
        elif self.v2.isChecked():
            text=self.matn.text()
            self.kur.execute("SELECT * FROM talaba WHERE name=?",(text,))
        elif self.v3.isChecked():
            text=int(self.matn.text())
            self.kur.execute("SELECT * FROM talaba WHERE score=?",(text,))
        ls=self.kur.fetchall()
        self.table.setRowCount(len(ls))
        for i in range(len(ls)):
            self.table.setItem(i,0,QTableWidgetItem(str(ls[i][0])))
            self.table.setItem(i,1,QTableWidgetItem(str(ls[i][1])))
            self.table.setItem(i,2,QTableWidgetItem(str(ls[i][2])))
        self.matn.clear()
    def create(self):
        self.kur.execute("""CREATE TABLE IF NOT EXISTS talaba
                            (id NUMERIC,name TEXT,score INTEGER)""")
        self.con.commit()
    def insert(self,a,b,c):
        self.kur.execute("INSERT INTO talaba VALUES(?,?,?)",(a,b,c))
        self.con.commit()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())
oyna.con.close()