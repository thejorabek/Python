#%% if-1
a=int(input("a="))
if a>0:
    a+=1
    print("natija:",a)
else:
    print("natija:",a)
    
#%% if-2
a=int(input("a="))
if a>0:
    a+=1
    print("natija:",a)
else:
    a-=2
    print("natija:",a)
    
#%% if-3
a=int(input("a="))
if a>0:
    a+=1
    print("natija:",a)
elif a<0:
    a-=2
    print("natija:",a)
else:
    print("natija: ",a+10)
    
#%% if-4
son1=int(input("1-son: "))
son2=int(input("2-son: "))
son3=int(input("3-son: "))
soni=0
if son1>0:
    soni+=1
if son2>0:
    soni+=1
if son3>0:
    soni+=1
print("musbatlari soni: {}".format(soni))    
#%% if-5
son1=int(input("1-son: "))
son2=int(input("2-son: "))
son3=int(input("3-son: "))
man=0
mus=0
if son1<0:
    man+=1
elif son1>0:
    mus+=1
if son2<0:
    man+=1
elif son2>0:
    mus+=1
if son3<0:
    man+=1
elif son3>0:
    mus+=1
print("manfiylari soni: {}\nmusbatlari soni: {}".format(man,mus))

#%% if-6
a=int(input("a="))
b=int(input("b="))
if a>b:
    print("max =",a)
elif a<b:
    print("max =",b)
else:
    print("ular teng")
    
#%% if-7
a=int(input("a="))
b=int(input("b="))
if a>b:
    print("min =",b,"\n2-son")
elif a<b:
    print("min =",a,"\n1-son")
else:
    print("ular teng")

#%% if-8
a=int(input("a="))
b=int(input("b="))
if a>b:
    print("natija: ",a,b)
elif a<b:
    print("natija:",b,a)
else:
    print("ular teng")

#%% if-9
a=int(input("a="))
b=int(input("b="))
if a<b:
    a=a+b
    print("a son: {}\nb son: {}".format(a,b))

#%% if-10
a=int(input("a="))
b=int(input("b="))
if a!=b:
    a=a+b
    b=a
    print("\nnatija:\na={}\nb={}".format(a,b))
elif a==b:
    a=0
    b=0
    print("\nnatija:\na={}\nb={}".format(a,b))

#%% if-11
a=int(input("a="))
b=int(input("b="))
if a!=b:
    if a>b:
        a=a
        b=a
    else:
        a=b
        b=b
    print("\nnatija:\na={}\nb={}".format(a,b))
elif a==b:
    a=0
    b=0
    print("\nnatija:\na={}\nb={}".format(a,b))

#%% if-12
a=int(input("1-son: "))
b=int(input("2-son: "))
c=int(input("3-son: "))
min=a
if b<c and b<a:
    min=b
    print("\nmin={}".format(min))
elif c<b and c<a:
    min=c
    print("\nmin={}".format(min))  
    
#%% if-13
a=int(input("1-son: "))
b=int(input("2-son: "))
c=int(input("3-son: "))
if a>b and a<c or a<b and a>c:
    middle=a
    print("\nmiddle={}".format(middle))
elif b>a and b<c or b<a and b>c:
    middle=b
    print("\nmiddle={}".format(middle))
elif c<a and c>b or c>a and c<b:
    middle=c
    print("\nmiddle={}".format(middle))
    
#%% if-14
a=int(input("1-son: "))
b=int(input("2-son: "))
c=int(input("3-son: "))
if a>b and a<c or a<b and a>c:
    middle=a
    if b<c:
        print("\nkichigi={}\nkattasi={}".format(b,c))
    elif b>c:
        print("\nkichigi={}\nkattasi={}".format(c,b))    
elif b>a and b<c or b<a and b>c:
    middle=b
    if a>c:
        print("\nkichigi={}\nkattasi={}".format(c,a))
    elif a<c:
        print("\nkichigi={}\nkattasi={}".format(a,c))
elif c<a and c>b or c>a and c<b:
    middle=c
    if b<a:
        print("\nkichigi={}\nkattasi={}".format(b,a))
    elif b>a:
        print("\nkichigi={}\nkattasi={}".format(a,b))

#%% if-15
# a=int(input("1-son: "))
# b=int(input("2-son: "))
# c=int(input("3-son: "))
# if a+b>a+c and a+b>b+c:
#     print("natija: ",a,b)
# elif a+c>a+b and a+c>b+c:
#     print("natija: ",a,c)
# elif b+a>a+c and b+a>b+c:
#     print("natija: ",a,b)
# elif b+c>a+c and b+c>b+c:
#     print("natija: ",a,b)
# elif c+a>a+c and c+a>b+c:
#     print("natija: ",a,b)
# elif c+b>a+c and c+b>a+b:
#     print("natija: ",a,b)

#%% if-16
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print("natija: a={} b={} c={}".format(2*a,2*b,2*c))
else:
    if a>0:
        a=-a
    else:
        a=-a
    if b>0:
        b=-b
    else:
        b=-b
    if c>0:
        c=-c
    else:
        c=-c
    print("natija: a={} b={} ={}".format(a,b,c))

#%% if-17
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c or a>b>c:
    print("natija: a={} b={} c={}".format(2*a,2*b,2*c))
else:
    if a>0:
        a=-a
    else:
        a=-a
    if b>0:
        b=-b
    else:
        b=-b
    if c>0:
        c=-c
    else:
        c=-c
    print("natija: a={} b={} ={}".format(a,b,c))

#%% if-18
a=int(input("1-son: "))
b=int(input("2-son: "))
c=int(input("3-son: "))
if a==b:
    print("3-son")
elif a==c:
    print("2-son")
elif b==c:
    print("1-son")

#%% if-19
a=int(input("1-son: "))
b=int(input("2-son: "))
c=int(input("3-son: "))
d=int(input("4-son: "))
if b==c==d:
    print("1-son")
elif a==c==d:
    print("2-son")
elif a==b==d:
    print("3-son")
elif a==b==c:
    print("4-son")
    
#%% case-1
kun=int(input("1-7 son tanlang: "))
if kun==1:
    print("Dushanba")
elif kun==2:
    print("Seshanba")
elif kun==3:
    print("Chorshanba")
elif kun==4:
    print("Payshanba")
elif kun==5:
    print("Juma")
elif kun==6:
    print("Shanba")
elif kun==7:
    print("Yakshanba")
else:
    print("Bunday kun mavjud emas")

#%% case-2
baho=int(input("bahoni kiriting: "))
if baho==1:
    print("Yomon")
elif baho==2:
    print("Qoniqarsiz")
elif baho==3:
    print("Qoniqarli")
elif baho==4:
    print("Yaxshi")
elif baho==5:
    print("A'lo")
else:
    print("Xato!")
    
#%% case-3
oy=int(input("oyni raqam sifatida kiriting: "))
if oy==12 or oy==1 or oy==2:
    print("Qish")
elif oy==3 or oy==4 or oy==5:
    print("Bahor")
elif oy==6 or oy==7 or oy==8:
    print("Yoz")
elif oy==9 or oy==10 or oy==11:
    print("Kuz")
    
#%% case-4
oy=int(input("oyni raqam sifatida kiriting: "))
if oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12:
    print("Ushbu oyda 31 kun mavjud")
elif oy==4 or oy==6 or oy==9 or oy==11:
    print("Ushbu oyda 30 kun mavjud")
elif oy==2:
    yil = int(input("Bu raqam fevral oyiga tegishliligi sabab kabisa yiliga tekshiramiz. Yilni kiriting: "))
    if (yil%400 == 0):
        print("Ushbu yilga tegishli fevral oyida 29 kun mavjud")
    elif (yil%100 == 0):
        print("Ushbu yilga tegishli fevral oyida 28 kun mavjud")
    elif (yil%4 == 0):
        print("Ushbu yilga tegishli fevral oyida 29 kun mavjud")
    else:
        print("Ushbu yilga tegishli fevral oyida 28 kun mavjud")

#%% case-5
a=int(input("1-sonni kiriting: "))
b=int(input("Amal: 1-qo'shish\n\t  2-ayirish\n\t  3-bo'lish\n\t  4-ko'paytirish\n\t: "))
c=int(input("2-sonni kiriting: "))
if b==1:
    d=a+c
    print("{} + {} = {}".format(a,c,d))
elif b==2:
    d=a-c
    print("{} - {} = {}".format(a,c,d))
elif b==3:
    d=a/c
    print("{} / {} = {:.1f}".format(a,c,d))
elif b==4:
    d=a*c
    print("{} * {} = {}".format(a,c,d))

#%% case-10
print("Salom. Hozir robot janubga qaragan holda turibdi. ")
tomon=input("Tomonni kiriting: 's'-shimol\n\t\t\t\t   'j'-janub\n\t\t\t\t   'q'-sharq\n\t\t\t\t   'g'-garb\n\t\t\t\t   :")
buyruq=input("Buruqni kiriting: 0-harakatni davom ettir\n\t\t\t\t   1-chapga buril\n\t\t\t\t   2-o'nga buril\n\t\t\t\t   :")
if tomon=='s':
    if buyruq==0:
        print("robot shimol tomonga burildi ")
elif tomon=='j':
    print("robot janub tomonga burildi")
elif tomon=='q':
    print("robot sharq tomonga burildi")
elif tomon=='g':
    print("robot g'arb tomonga burildi")

#%% 1-misol
son=int(input("n="))
for juft in range(1, son):
    if(juft%2==0):
        print("{}".format(juft))

#%% 2-misol
son=int(input("n="))
for toq in range(1, son):
    if(toq%2!=0):
        print("{}".format(toq))

#%% 3-misol
for i in range(10,100):
    if i%2!=0:
        print(i, end=" ")

#%% 5-misol
son=input("son = ")
teskari=''
for i in range(len(son), 0, -1):
   teskari+=son[i-1]
print('natija =', teskari)

#%% 6-misol
n=int(input("n=")) #n=4
m=(2*n)-2 #m=(2*4)-2=6
for i in range(0,n): #(0,4)
    for j in range(0, m): #(0,6) 
        print(end=" ") 
    #m=m-1 #6=6-1
    for j in range(0,i+1): #(0,)
        print("*", end=" ")
    print(" ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    