#%% 1
class Hayvon():
    def __init__(self,nomi):
        self.name=nomi
class Yirtqich(Hayvon):
    def ovlash(self):
        print(self.name,"yashash uchun ovlaydi")
    def yugurish(self):
        print(self.name,"o'ljaga yetib olish uchun yuguradi")
    def uxlash(self):
        print(self.name,"kuch yig'ish uchun uxlaydi")
class Otxor(Hayvon):
    def yugurish(self):
        print(self.name,"yirtqichdan qochish uchun yuguradi")
    def avlodQoldirish(self):
        print(self.name,"qirilib ketmaslik uchun avlod qoldiradi")
    def eshitish(self):
        print(self.name,"yirtqichlarni eshitadi")
sher=Yirtqich("Alex")
sher.ovlash()
sher.uxlash()
sher.yugurish()
kiyik=Otxor("Bambi")
kiyik.avlodQoldirish()
kiyik.eshitish()
kiyik.yugurish()

#%% 2
class Shape():
    def __init__(self,name):
        self.name=name
class Line(Shape):
    def show(self):
        print("* "*10)
class Triangle(Shape):
    def show(self):
        n=int(input("n="))
        for i in range(n):
            for j in range(i):
                if i==0 or i==n-1 or j==i-1 or j==0:
                    print("* ",end="")
                else:
                    print(end="  ")
            print()
class Rectangle(Shape):
    def show(self):
        n=int(input("n="))
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or j==n-1 or j==0:
                    print("* ",end="")
                else:
                    print(end="  ")
            print()
class NullShape(Shape):
   def show(self):
       print("Bo'sh shakl")
ob=Line("Chiziq")
ob.show()
ob1=Triangle("Uchburchak")
ob1.show()
ob2=Rectangle("To'rtburchak")
ob2.show()
ob3=NullShape("NullShape")
ob3.show()

lst=[ob,ob1,ob2]
k=0
nomi=input("Shakl nomini kiriting: ")
for i in lst:
    if i.name==nomi:
        i.show()
        k=0
        break
    else:
        k=1
if k==1:
    ob3.show()
    
#%%
new=[]
class Int():
    def __init__(self):
        new.append(int(input("Butun sonni kiriting: ")))
class Float(Int):
    def __init__(self):
        print("1-int yoki float 2-bool")
        a=int(input("a="))
        if a==1:
            super().__init__()
        if a==2:
            new.append(float(input("Haqiqiy sonni kiriting: ")))
class Float(Int):
    def __init__(self):
        print("1-int 2-float")
        a=int(input("a="))
        if a==1:
            super().__init__()
        if a==2:
            new.append(float(input("Haqiqiy sonni kiriting: ")))
        else:
            
            
            
            
        