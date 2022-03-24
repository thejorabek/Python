#%% Function
def summary(a,b):
    return a+b
print(summary(10, 15))
print(summary(3.14159, -125))
print(summary("Salom", "O'rdak"))
#print(summary("hello", 10)
a=int()
a='salom'
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    print(f"{n}!={s}")
fact(int(input("n=")))

#%%
def salomlashish():
    print("salom "*2)
def xayrlashish():
    return "Alvido "*5
def main():
    salomlashish()
    print(xayrlashish())
main()
def enter(ls)->list:
    for i in range(int(input("n="))):
        ls.append(int(input("son=")))
    return ls
ls=list()
print(enter(ls))

#%%
def math(a,b):
    return {str(a+b):[a-b,a*b,a/b]}
a=math(100,75)
print(a,type(a))

#%% Recursive function
def son(num):
    if num==1:
        return 1
    elif num>1:
        return num+son(num-1)
print(son(5))

#%%
def printf1(son):
    if son>0:
        print(son,end=" ")
        printf1(son-1)
def printf2(son):
    if son>0:
        printf2(son-1)
        print(son,end=" ")
printf1(5)
print()
printf2(5)

#%% Lambda function
def s(n):
    return n*n
print(s(2))
new=lambda x: x*x
print(new(10))

son=lambda a,b,c: a//b*c
print(son(20,10,30))

n=lambda a,b,c: [a+b,a-10,b*20,c/(a+b)]
print(n(1,2,3))

ls=[i for i in range(1,11) if i%2==0]
print(ls)

#%% 1-misol
def tub(n):
    k=0
    for i in (2,n/2):
        if n%i!=0:
            k+=1
    if k==0:
        print("tub")
    else:
        print("tub emas")
tub(23)

#%% 2-misol
def teskari(N)->int:
    if N>0:
        print(son%10,end=" ")
        teskari(son//10)
son=int(input("n="))
teskari(son)

#%%
def teskari(N)->int:
    if N>0:
        teskari(son//10)
        print(son%10,end=" ")
teskari(int(input("N=")))

#%%
def enter(ls)->list:
    for i in range(int(input("n="))):
        ls.append(int(input("son=")))
    return ls
ls=list()
print(enter(ls))

# print() -\
# len()    -| ==> built_in function
# zip()   -/

#%% TRY | EXCEPT | FINALLY
# a=int(input("son kirit: "))
# count=0
# while a>0:
#     qoldiq=a%10
#     count+=qoldiq
#     a=a//10
# print(count)
# "-------------------------"
# #xato --> a isn't iterable
# a=10 
# for v in a:
#     print(v)
# "-------------------------"
# a="salom"
# for f in a:
#     print(f)
# f=(input("kirit: "))
# print(f)
# "--------------------------"
# a=list()
# b=[1,3,4,True,"salom",22.4]
# b=b*3
# print(len(b))
# "---------------------------"
























































































































































































































