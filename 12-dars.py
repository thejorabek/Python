# #%% Time module
import time as t
t.sleep(0.5)
print(5)
t.sleep(0.5)
print(4)
t.sleep(0.5)
print(3)
t.sleep(0.5)
print(2)
t.sleep(0.5)
print(1)
t.sleep(0.5)
print(0)
print(t.asctime())

# #%% Polimorfizm
# print(2+3,2.14+3.14,True+False,"salom"+"xayr")
# print([1,2,3,4]+[5,6,7,8,9])
# print(len("salom"),len([1,2,3,4]),len({1,2,3,4}))

# #%% Abstraction
# from abc import ABC,abstractmethod
# class Jonzot(ABC):
#     def Name(self,nomi):
#         self.name=nomi
#         @abstractmethod
#         def test(self,a):
#             print("Test for Abstraction method")
# class Hayvon(Jonzot):
#     def test(self):
#         # super().test(100)
#         print("Test for Inheritance class")
# ob=Hayvon()
# ob.Name("Ayiq")
# ob.test()

# #%% Try-Except
# try:
#     print(2/2)
# except ZeroDevisionError:
#     print("Nolga bo'lib bo'lmaydi")
# except:
#     print("Qandaydir xatolik")
# else:
#     print("Xatolik yo'q")
# print("salom")
# print("xayr")

# #%%
# try:
#     f=open("exam")
#     try:
#         f.write("Imtihon boshlandi")
#     except:
#         print("Faylga yozish jarayonida xatolik")
#     finally:
#         print("Fayl yopildi")
#         f.close()
# except:
#     print("Fayl ochish jarayonida xatolik")    

#%%
# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# oyna=QWidget()
# oyna.setWindowTitle("My first application") #Title
# oyna.setGeometry(300,300,500,300) # (X,Y,width,height)
# #oyna.setFixedSize(500,300)
# #oyna.move(500,500) # (X,Y)
# yozuv=QLabel("Bir narsa",oyna)
# yozuv.move(50,100)
# yozuv.setFont(QFont("JetBrains Mono",13))
# kiritish=QLineEdit(oyna)
# kiritish.move(50,50)
# kiritish.setFont(QFont("JetBrains Mono",13))
# ok=QPushButton("Bajarish",oyna)
# ok.move(50,150)
# ok.setFont(QFont("JetBrains Mono",13))
# def run():
#     text=str(kiritish.text())
#     yozuv.setText(text)
#     kiritish.setText("")
# ok.clicked.connect(run)
# oyna.show()
# sys.exit(app.exec_())

#%%
# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
# from PyQt5.QtGui import QFont
# import sys

# app=QApplication(sys.argv)

# oyna=QWidget()
# oyna.setWindowTitle("Registration") #Title
# oyna.setGeometry(300,300,460,250) # (X,Y,width,height)

# yozuv=QLabel("login",oyna)
# yozuv.move(50,48)
# yozuv.setFont(QFont("JetBrains Mono",18))
# yozuv=QLabel("password",oyna)
# yozuv.move(50,100)
# yozuv.setFont(QFont("JetBrains Mono",18))
# yozuv=QLabel("Forget your login or password ?",oyna)
# yozuv.move(205,200)
# yozuv.setFont(QFont("JetBrains Mono",8))

# kiritish=QLineEdit(oyna)
# kiritish.move(200,50)
# kiritish.setFont(QFont("JetBrains Mono",15))
# kiritish=QLineEdit(oyna)
# kiritish.move(200,100)
# kiritish.setFont(QFont("JetBrains Mono",15))

# ok=QPushButton("Sign in",oyna)
# ok.move(200,150)
# ok.setFont(QFont("JetBrains Mono",12))
# ex=QPushButton("Cancel",oyna)
# ex.move(330,150)
# ex.setFont(QFont("JetBrains Mono",12))

# oyna.show()
# sys.exit(app.exec_())
