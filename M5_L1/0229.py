# account https://robocontest.uz/profile/pasago
#misol https://robocontest.uz/tasks/0229


import math
a, b = map(int, input().split())

A = (a + b) / 2  
G = math.sqrt(a * b)

if A > G:
    print(">")
elif G > A:
    print("<")
else:
    print("=")