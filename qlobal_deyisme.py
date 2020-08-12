def asagi(r):
    s=0
    for i in r:
        s+=r[i]
    return s/n


def yuxari(r):
    max=m
    for i in r:
        if r[i]>max:
            max=r[i]
    return max

a=int(input("Ruslanin qiymeti:  "))
b=int(input("Kamranin qimeti :  "))
c=int(input("Mehdinin qiymeti : "))

rus={"t1":a,"t2":b,"t3":c}
n=len(rus)
m=0

print("Orta qiymet : ",asagi(rus))

print("Yuksek qiymet :", yuxari(rus))
