def ayristirici(sayi) -> bool:
    a = str(sayi)  
    s1 = sum(int(s) for s in a[:3])  
    s2 = sum(int(s) for s in a[3:])  
    return s1 == s2  

def hesapla(a):
    
    onceki_bilet = str(int(a) - 1).zfill(6) 
    sonraki_bilet = str(int(a) + 1).zfill(6)  

    if ayristirici(onceki_bilet) or ayristirici(sonraki_bilet):
        return "Yes"
    return "No"

a = input().strip() 
print(hesapla(a))
