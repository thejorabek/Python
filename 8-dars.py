#%% Object Oriented Programming
'''
1) Inkapsulatsiya
2) Vorislik (Merosxorlik)
3) Polomorfizm
4) Abstraksiya
'''

#%%
class Odam():
    a="qo'l"
    b="oyoq"
    c="ko'z"
    d="quloq"
    def teginish(self):
        print(f"{self.a} bilan teginamiz")
    def yurish(self):
        print(f"{self.b} bilan yuramiz")
    def korish(self):
        print(f"{self.c} bilan ko'ramiz")
    def eshitish(self):
        print(f"{self.d} bilan eshitamiz")
Sardor=Odam()
Sardor.teginish()
Sardor.yurish()
Sardor.korish()
Sardor.eshitish()
print(type(Sardor))
print(Sardor)

#%%
class Meva():
    nomi="olma"
    narxi=15000
    turi="Golden"
    def print_info(self):
        print(f"Meva nomi: {self.nomi}")
        print(f"Meva narxi: {self.narxi}")
        print(f"Meva turi: {self.turi}")
    def add_fruit(self,name,price,tip):
        self.nomi=name
        self.narxi=price
        self.turi=tip
olma=Meva()
print(olma.nomi,olma.narxi,olma.turi)
olma.print_info()
anor=Meva()
anor.nomi="Anor"
anor.narxi=23000
anor.turi="Shirin"
anor.print_info() 
gilos=Meva()
gilos.add_fruit(input("Name:"), int(input("Price:")), input("Type:"))
gilos.print_info()       

#%% Counter Strike
class Player():
    def __init__(self,name):
        self.name=name
        self.health=100
        self.armour=""
    def info(self):
        print(self.name,self.health,self.armour)
    def armor(self,qurol):
        self.armour=qurol
    def otish(self,obj):
        if self.health!=0:
            print(self.name,"-->pix",obj.name,"pax")
            obj.health-=50
            if obj.health<=0:
                print(self.name,"WINS!!!")
        else:
            print(self.name,"is deadXXX")
Terrorist=Player("Abdulla")
Terrorist.armor("AK47")
Terrorist.info()
CounterTerrorist=Player("Farrux")
CounterTerrorist.armor("MK4")
CounterTerrorist.info()
Terrorist.otish(CounterTerrorist)
Terrorist.info()
CounterTerrorist.info()
CounterTerrorist.otish(Terrorist)
Terrorist.info()
CounterTerrorist.info()
Terrorist.otish(CounterTerrorist)
Terrorist.info()
CounterTerrorist.info()
CounterTerrorist.otish(Terrorist)
Terrorist.info()
CounterTerrorist.info()

#%%
class Talaba():
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
class Kurs():
    def __init__(self, nomi, oqituvchi):
        self.nomi = nomi
        self.oqituvchi = oqituvchi
        self.talabalar_soni = 0
        self.talabalar = []
    def add_student(self, s):
        self.talabalar_soni += 1
        self.talabalar.append(s.ism+' '+s.familiya+' '+str(s.yosh))
    def delete_student(self, name):
        new=str()
        for i in self.talabalar:
            if name in i:
                new=i
        if new!='':
            self.talabalar.remove(new)
            self.talabalar_soni-=1
    def info(self):
        print(f"{self.nomi} {self.oqituvchi} {self.talabalar_soni} {self.talabalar}")
Komol = Talaba("Komol", "Sattorov", 15)
Said = Talaba("Said", "Qahxorov", 18)
Ali = Talaba("Ali", "Amirov", 17)

Flutter = Kurs("Flutter","Saud")
Golang = Kurs("GO","Nurali")

Flutter.add_student(Komol)
Flutter.add_student(Said)
Flutter.add_student(Ali)
Flutter.info()
Flutter.delete_student(input("name: "))
Flutter.info()

# Golang.add_student(Kamron)
# Golang.add_student(Jamol)
# Golang.add_student(Jamila)
# Golang.add_student(Axrorxoja)
Golang.info()
Golang.delete_student(input("name: "))
Golang.info()
print(f"{Flutter.nomi} kursida {Flutter.talabalar_soni}ta  talaba o'qiydi")
print(f"{Golang.nomi} kursida {Golang.talabalar_soni}ta  talaba o'qiydi")
