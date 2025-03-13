# account https://robocontest.uz/profile/pasago
#misol https://robocontest.uz/tasks/0145

def en_buyuk_cevreli_ucgen(n, cubuklar):
    cubuklar.sort(reverse=True)
    for i in range(n - 2):
        a, b, c = cubuklar[i], cubuklar[i + 1], cubuklar[i + 2]
        if a < b + c:  
            print(c, b, a)  
            return
    print(-1)


n = int(input())
cubuklar = list(map(int, input().split()))

en_buyuk_cevreli_ucgen(n, cubuklar)