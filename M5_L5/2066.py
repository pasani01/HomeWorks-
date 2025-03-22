from itertools import product

def Hesapla(a,b,c):
    belgeler=["+","-","*"]
    dusuksayi=0

    for belge1,belge2 in product(belgeler,repeat=2):

        dusuk=eval(f"{a} {belge1} {b} {belge2} {c}")
        if dusuk< dusuksayi:
            dusuksayi=dusuk
    else :
        return dusuksayi

a=int(input())
b=int(input())
c=int(input())

print(Hesapla(a,b,c))