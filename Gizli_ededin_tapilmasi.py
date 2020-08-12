a=34

print("1-100 arasi gizli ededi tapin ")
k=0

while True:
    b=int(input())
    k=k+1
    if b<a:
        print ("Gizli ededden yuxari ededi secdiniz")
    elif b>a:
        print("Gizli ededden asagi ededi secdiniz")
    else:
        break

print("Tebrikler!!! Siz Gizli ededi tapdiniz.")
