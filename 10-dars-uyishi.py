import colorama as c
import time
import random as rand
print(c.Style.BRIGHT)
n=int()



def ColorChange(n,i):
    if n==1:
        print(c.Fore.RED,i,end='')
        time.sleep(0.3)
    if n==2:
        print(c.Fore.GREEN,i,end='')
        time.sleep(0.3)
    if n==3:
        print(c.Fore.BLUE,i,end='')
        time.sleep(0.3)
    if n==4:
        print(c.Fore.YELLOW,i,end='')
        time.sleep(0.3)
    if n==5:
        print(c.Fore.CYAN,i,end='')
        time.sleep(0.3)



masala1="Birinchi masala tayyor:"
for i in masala1:
    n=rand.randint(1,5)
    ColorChange(n,i)
print() 
matn=input("Matnni kiriting: ")
for i in matn:
    if i in 'AaBbCcDdEeFfGgHh':
        print(c.Fore.RED,i,end='')
        time.sleep(0.3)
    elif i in 'IiJjKkLlMmNnOoPp':
        print(c.Fore.YELLOW,i,end='')
        time.sleep(0.3)
    elif i in 'QqRrSsTtUuVvWwXxYyZz':
        print(c.Fore.GREEN,i,end='')
        time.sleep(0.3)
print(c.Style.RESET_ALL)



print(c.Style.BRIGHT)
masala2="Ikkinchi masala ham tayyor:"
for i in masala2:
    n=rand.randint(1,5)
    ColorChange(n,i)
print()
son=input("son: ")
list1=str()
for i in son:
    list1+=str((int(i)+7)%10)
for i in list1:
    n=rand.randint(1,4)
    ColorChange(n,i)
print(c.Style.RESET_ALL) 


print(c.Style.BRIGHT)
masala3='Uchinchi masala ham tayyor:'
for i in masala3:
    n=rand.randint(1,5)
    ColorChange(n,i)
print()
import random as rand
from random import choice
list1 = list()
for i in range (100):
    i=rand.randint(100,1000)
    list1.append(i)
print(list1)
a=choice(list1)
print(f"tanlangan son: {a}")
for i in list1:
    if list1.index(i) == list1.index(a):
        break
    if i%2 == 0:
        print(' ')
        n=rand.randint(1,5)
        ColorChange(n,i)

        
print(c.Style.BRIGHT)
masala4="\nTortinchi masala ham tayyor: "
for i in masala4:
    n=rand.randint(1,5)
    ColorChange(n,i)
print()
list2=list()
for i in range(1000):
    i=rand.randint(1,1000000)
    list2.append(i)
print(list2)
b=choice(list2)
k=0
print(f"Tanlangan son: {b}")
gapde="Karrochi hozir sizga shu sondan keyingi tub sonlarni chiqarib berishim keremi?"
for i in gapde:
    n=rand.randint(1,5)
    ColorChange(n,i)
print('\nLoading',end='')
time.sleep(1)
print('.',end='')
time.sleep(1)
print('.',end='')
time.sleep(1)
print('.',end='')
time.sleep(1.5)
print()
for i in list2:
    if i == b:
        k+=1
    if k==1 and i!=b:
        print(i,end='  ')