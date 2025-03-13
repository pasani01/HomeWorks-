# account https://robocontest.uz/profile/pasago
#misol https://robocontest.uz/tasks/0202


d={
    0:6,
    1:2,
    2:5,
    3:5,
    4:4,
    5:5,
    6:6,
    7:3,
    8:7,
    9:6
}
def Goslemci(sayi )->int:
    if sayi in d.keys():
        return d[sayi]

a=input()
s=0
for i in a:
    s+=Goslemci(int(i))
print(s)
