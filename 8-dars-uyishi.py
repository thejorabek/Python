class Kitob():
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.muallifi=b    
        self.narxi=c    
        self.nashri=d
    def Info(self):
        if self.nashri[0]>='A' and self.nashri[0]<='H':
            print("""Nomi: {}
Muallifi: {}
Narxi: {}
Nashri: {}""".format(self.nomi,self.muallifi,self.narxi,self.nashri))
# print("1-kitob:")
# k1=Kitob(input("Nomi: "), input("Muallifi: "), int(input("Narxi: ")), input("Nashri: "))
k1=Kitob("Python","Paulo",45000,"Hilol")
# print("2-kitob:")
# k2=Kitob(input("Nomi: "), input("Muallifi: "), int(input("Narxi: ")), input("Nashri: "))
k2=Kitob("C","Stiven",50000,"Asaxiy")
# print("3-kitob:")
# k3=Kitob(input("Nomi: "), input("Muallifi: "), int(input("Narxi: ")), input("Nashri: "))
k3=Kitob("Golang","Alisher",78000,"Sharq")
# print("4-kitob:")
# k4=Kitob(input("Nomi: "), input("Muallifi: "), int(input("Narxi: ")), input("Nashri: "))
k4=Kitob("Flutter","Bobur",34000,"Yulduz")
# print("5-kitob:")
# k5=Kitob(input("Nomi: "), input("Muallifi: "), int(input("Narxi: ")), input("Nashri: "))
k5=Kitob("Java","Shoxrux",63000,"Umid")
# print("-----------------")
k1.Info()
k2.Info()
k3.Info()
k4.Info()
k5.Info()

#%%
class Computer():
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.rami=b
        self.narxi=c
        self.protsessori=d
    def Info(self):
        if self.rami>=4 and self.rami<=16:
            print("""Nomi: {}
RAM: {}
Narxi: {}
Protsessori: {}""".format(self.nomi, self.rami, self.narxi,self.protsessori))
# print("1-Kompyuter:")
# k1=Computer(input("Nomi: "),int(input("RAMi: ")),int(input("Narxi: ")),input("Protsessori: "))
k1=Computer("Lenovo", 12, 1000, "Intel")
# print("2-Kompyuter:")
# k2=Computer(input("Nomi: "),int(input("RAMi: ")),int(input("Narxi: ")),input("Protsessori: "))
k2=Computer("MacBook", 32, 4000, "M1")
# print("3-Kompyuter:")
# k3=Computer(input("Nomi: "),int(input("RAMi: ")),int(input("Narxi: ")),input("Protsessori: "))
k3=Computer("MacBook", 64, 6000, "M1 Max")
# print("4-Kompyuter:")
# k4=Computer(input("Nomi: "),int(input("RAMi: ")),int(input("Narxi: ")),input("Protsessori: "))
k4=Computer("Dell", 8, 2000, "Intel")
# print("-----------------")
k1.Info()
k2.Info()
k3.Info()
k4.Info()