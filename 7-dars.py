#%% FILE 
f=open("F32","w")
f.write("Foundation 32.\n"+"Imtihon yaqin!")
f.writelines("""Chopilish ehtimoli juda kuchli!!!
             Yaxshi tayyorlanish kerak
             HAHAHAHAHAHAHAHAHAHAHAHAHA""")
f.close()
#%% FILE read, readline, readlines
with open("F32","r") as p:
    new=p.read(10)
    print(p.tell())
print(new)
with open("F32","r") as fp:
    text=fp.readline()
    text2=fp.readline()
    print("{1}",text2,"(1)")
    print(fp.tell())
print(text)
with open("F32","r") as read:
    matn=read.readlines()
print(*matn)    
    
#%% 1-misol
f=open("Letters","w")
f.write("#include<iostream>int main(){ return 0; }")
f.close()
jami=0
with open("Letters","r") as p:
    new=p.read()
for i in new:
    if i in 'qwertyuiopasdfghjjklzxcvbnm':
        jami+=1
print(jami)

#%% 2-misol
f=open("Number","w")
f.write("#include<iostream>int main(){ return 0; }")
f.close()
jami=0
with open("Number","r") as p:
    new=p.read()
for i in new:
    if i in '0123456789':
        jami+=1
print(jami)
        
#%% 3-misol
new=list()
f=open(input("fayl nomini kiriting: "),"w")
f.write("#include<iostream>int main(){ return 0; }")
for i in f.name:
    new.append(i)
f.close()
#print(new)
new=sorted(new)
f=open("new2","w")
for i in range(len(new)):
    f.write(new[i]+' ')
f.close()
f=open("new1","w")
for i in range(len(new)):
    f.write(new[-i-1]+' ')
f.close()

#%% 4-misol
new=list()
f=open(input("fayl nomini kiriting: "),"w")
f.write("#include<iostream>int main(){ return 0; }")
for i in f.name:
    new.append(i)
f.close()
#print(new)
new=sorted(new)
f=open("new2","w")
for i in range(len(new)):
    f.write(new[i]+' ')
f.close()
f=open("new1","w")
for i in range(len(new)):
    f.write(new[-i-1]+' ')
f.close()
