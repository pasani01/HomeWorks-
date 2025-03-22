n = int(input())
if n > 0 :
    print(int((n*(1+n))/2))
elif n < 0:
    print(int((abs(n)+2)*(1+n)/2))
else:
    print(1)
