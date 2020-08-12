import tkinter as tk # tkinter paketini import edirik

hesab=tk.Tk()  # tkinteri deyiskene tanimlayiriq
hesab.title("RUSLANIN KALKULYATORU") # ad yerlesdiririk
hesab.resizable(0,0)  # pencere olculerini deyisilmek ssaxlayiriq.(0,0) yerine ("False,False") de yaza bilerik

def kalkulyator(x):  # kalkulyatorun islemesi ucun funksiyani teyin edirik ve evaldan istifade edirik
    global kal   # kal sozluyunu glaobala daxil edirik ki diger funksiya icerisinde deyise bilek
    kal=kal+str(x)
    variable.set(kal)
    
def sil():
    global kal  # burda da hemcinin
    kal=""
    variable.set(kal)

def cem():
    
    global kal
    kal=str(eval(kal))
   

    variable.set(kal)

kal=""  # kal ucun bos bir setir tipi yaradiriq sonradan bunun uzerine yazilmasi ucun

duyme1=tk.Button(hesab,text="1",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(1))
duyme1.grid(row=3,column=0)
duyme2=tk.Button(hesab,text="2",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(2))
duyme2.grid(row=3,column=1)
duyme3=tk.Button(hesab,text="3",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(3))
duyme3.grid(row=3,column=2)
duyme0=tk.Button(hesab,text="0",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(0))
duyme0.grid(row=4,column=0)
noqte=tk.Button(hesab,text=".",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator("."))
noqte.grid(row=4,column=1)
silduymesi=tk.Button(hesab,text="C",font=("arial",20,"bold"),bd=5,padx=20,command=sil)
silduymesi.grid(row=4,column=2)
toplama=tk.Button(hesab,text="+",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator("+"))
toplama.grid(row=1,column=4)
cixma=tk.Button(hesab,text="-",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator("-"))
cixma.grid(row=2,column=4)
vurma=tk.Button(hesab,text="*",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator("*"))
vurma.grid(row=3,column=4)
bolme=tk.Button(hesab,text="/",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator("/"))
bolme.grid(row=4,column=4)
beraberlik=tk.Button(hesab,text="=",font=("arial",20,"bold"),bd=5,padx=20,command=cem)
beraberlik.grid(row=5,columnspan=5)
variable=tk.StringVar()
duyme7=tk.Button(hesab,text="7",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(7))
duyme7.grid(row=1,column=0)
duyme8=tk.Button(hesab,text="8",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(8))
duyme8.grid(row=1,column=1)
duyme9=tk.Button(hesab,text="9",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(9))
duyme9.grid(row=1,column=2)
ekran=tk.Entry(hesab,font=("arial",20,"bold"),bd=20,textvariable=variable,justify="right")
ekran.grid(row=0,column=0,columnspan=10)
duyme4=tk.Button(hesab,text="4",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(4))
duyme4.grid(row=2,column=0)

duyme5=tk.Button(hesab,text="5",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(5))
duyme5.grid(row=2,column=1)

duyme6=tk.Button(hesab,text="6",font=("arial",20,"bold"),bd=5,padx=20,command=lambda:kalkulyator(6))
duyme6.grid(row=2,column=2)
# Qrafik arauzu isleyirik kenarda bunun olculeri yigilib test edilib
# Fonunu arial olcusunu 20 ve yazi tipini bold olaraq secirik
# her birinin geometrisini giririk test ederek
# bu kalkulyatora atri atri funksiya (def) elave etmek uzun is oldugundan lanbda funksiya novunden istifade edirik ve kalkulyator(x) deyisenine yonlendiririk
# Reqemleri yazdirmaq ucun ekran girintisi elave edirik fonunu teyin edirik  ve yazilarin sag tereden yazilmasi ucun justify="right" emrini yerine yetririk
hesab.mainloop()  # Programi islek veziyyete getririk







