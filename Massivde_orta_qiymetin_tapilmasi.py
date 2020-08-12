netice=[]
n=int(input("Sagirdlerin sayini daxil edin: "))
m=int(input("Qiymetlerin sayini daxil edin: "))

for i in range(n):
    netice.append([])

for i in range(n):
    r=netice[i]
    print("{}.sagirdin qiymetleri:".format(i+1))
    for j in range(m):
        r.append(int(input("Qiymet: ")))
        

print("Sagirdinlerin orta qiymetleri: ")
for i in range(n):
    s=0
    for j in range(m):
        s+=netice[i][j]
    print("{0:d}-{1:3.1f}".format(i+1,s/m))    
