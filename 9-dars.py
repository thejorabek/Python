#%%
class Karta():
	def __init__(self,nomi,raqam):
		self.name=nomi #public
		self.number=raqam #public
		self.__code="1111"
	def show(self):
		print(self.name,self.number,self.__code)
	def change(self,kod):
		a=input("Eski kodni kiriting: ")
		if a==self.__code:
			self.__code=kod
		else:
			print("Karta bloklandi. Siz karta egasi emassiz")
card1=Karta("Asaka",8600135465135615)
card1.show()
card1.name="Ipoteka"
card1.number=9089546545611554
card1.__code="7777"
card1.change("7777")
card1.show()
card_Karta__code="8888"
card1.show()

#%%
class A():
    name="Abdulla"
    __age=15
    def chiqarish(self): #getter
        print(self.name,self.__age)
    def set_name(self,a): #setter
        self.name=a
ob1=A()
ob1.chiqarish()
ob1.set_name("Davron")
ob1.chiqarish()

#%% Inheritance (vorislik)
class A(): #Base class
    a=10
class B(A): #Derived1 class
    a=78
    b=20
class C(B): #Derived2 class
    c=30
class D(C): #Derived3 class
    d=40
ob1=A()
ob1.a=100
print(ob1.a)
ob2=B()
print(ob2.a,ob2.b)
ob3=C()
ob3.a=200
print(ob1.a,ob3.a,ob3.b,ob3.c)
ob4=D()
print(ob4.a,ob4.b,ob4.c,ob4.d)

#%% Inheretance
class Director():
    def __init__(self,name,sname,age):
        self.name=name
        self.sname=sname
        self.age=age
    def show(self):
        print(f"Name: {self.name}\nSurname: {self.sname}\nAge: {self.age}")
class Xodim(Director):
    def __init__(self, name, sname, age, rank):
        super().__init__(name, sname, age)
        self.rank=rank
    def show(self):
        super().show()
        print("Rank:",self.rank)
Anvar=Director("Anvar", "Anvarov", 45)
Anvar.show()
Abdulla=Xodim("Abdulla", "Abdullayev", 23, "Slaser")
Abdulla.show()

#%% Polimorfizm
class Animal():
    def voice(self):
        print("Ovoz chiqarish")
class Birds(Animal):
    def voice(self):
        print("Chik chirik")
class Fish(Animal):
    pass
class Cat(Animal):
    def voice(self):
        print("Myau myau")
ob1=Animal()
ob1.voice()
ob1=Birds()
ob1.voice()
ob1=Fish()
ob1.voice()
ob1=Cat()
ob1.voice()
