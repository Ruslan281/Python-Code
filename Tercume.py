import tkinter as tk  # tkinteri import edirik
from googletrans import Translator  # bu paket vasitesile google translateden ingilsceden azerbaycan diline tercume edeciyik


p=tk.Tk()  # tkinteri tanimladiq
p.title("Tərcümə")  # adini daxil eledik        
p.geometry("530x300")   # olculerini daxil eledik
p.resizable(0,0)  # sabitlesdirdik

def tercume():  # sozleri ingilisceden tercume etmek ucun funksiyani teyin eledik yazdigim bu funksiya internet uzerinden axtaris neticesinde yazilib cunki googletrans bir basqa moduldurdur
    word=entry.get()
    translator=Translator(service_urls=["translate.google.com"])
    translation=translator.translate(word,dest="az")
    label1=tk.Label(p,text=f'Sözün tərcüməsi : {translation.text}',bg="yellow").grid(row=2,column=0)


soz=tk.Label(p,text="           Sözü daxil et ", font=("bold",25)).grid(row=0,column=0)


entry=tk.Entry(p,width=50).grid(row=1,column=0,ipadx=60,ipady=30,columnspan=3)


duyme=tk.Button(p,text="Tərcümə et",command=tercume).grid(row=2,column=2)

p.mainloop()

# bu program her bir yerde islemeye biler
# pip install googletrans
