import tkinter as tk  #  tkinteri import edirik daxile
from gtts import gTTS  # bu paketden online olaraq yazacaqimiz metini hansi dile sevireceyimize yardimci olacaq..google uzerinden isleyir
from playsound import playsound  # bunun komekliyi ile ise cevirdiyimiz sesleri yaddasda saxlayacayiq ses formasinda

p=tk.Tk() # Tk() tkinteri istifADESI ucun deyiskene atdiq

p.title("Yazini sese cevirme") # Programin adini yerlesdiririk
p.geometry("300x80")  # geometri olculerini daxil etdim
p.resizable(0,0)  # ekranla oynanilmamasi ucun sabitledim

def sesli_metin():  # Cevirme ucun funksiyani elave etdim
    text=giris.get()
    ses=gTTS(text=text,lang="tr")   # Azerbaycan dili olmadigi ucun "tr" turk dilini daxil etdim
    ses.save(r'C:\Users\KTB\Desktop\sesim.mp3')  # yazdigim qisa metni  masaustumde saxladim
    playsound(r'C:\Users\KTB\Desktop\sesim.mp3')  # yazdigim qisa metni masa ustumde sesli sekilde seslendirdim

ad=tk.Label(p,text="Yazacaqiniz sozu daxil edin  : ").grid(row=0,column=0)  # Programa asina olmaq ucun Yazacaqiniz sozu daxil edin : deye bir label yerlesdirdim
giris=tk.Entry(p).grid(row=1,column=0)  # sozleri daxil etmek ucun Entry elave eledim
duyme=tk.Button(p,text="Çevir",command=sesli_metin).grid(row=1,column=1)  # ve Duyme yerlesdirerek sozleri Sesli_metin funksiyasi vasitesile sesli formata cevirdik

p.mainloop()  # Programi islet veziyyete getirmek ucun Tkinterin mainloopundan istifade etdim
