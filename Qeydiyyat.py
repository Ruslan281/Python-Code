import tkinter as tk
import tkinter.ttk as ttk
 # Tkinteri import edirik
from openpyxl import *  # bu 3cu teref modulu import edirik excel formatinda yadda saxlamagi ucun
from tkinter.messagebox import showinfo  # melumat mesajlarinin verilmesi ucun

a=tk.Tk()  # a deyiskenine tanimladiq tkinteri
a.title("Qeydiyyat")  # Adini teyin eledik
a.configure(bg="black") # programin butun arxa fonunun rengini deyisirik
a.resizable(False,False)

def yaddas():
    ad=giris.get()
    familya=giris1.get()
    yas=giris2.get()

    excel=Workbook()
    excel1=excel.active

    excel1["A1"] = "Adiniz"
    excel1["B1"] = "Familyaniz"
    excel1["C1"] = "Yasiniz"
    excel1["A3"] = ad
    excel1["B3"] = familya
    excel1["C3"] = yas

    excel.save(r"C:\Users\KTB\Desktop\qeydiyyatim.xlsx")
    showinfo("Saxlamaq","Yaddasda saxlanildi")


def sil():   # Yalnis melumatlari silmek ucun sil funksiyasini teyin edirik

    giris.delete(0,tk.END)
    giris1.delete(0,tk.END)
    giris2.delete(0,tk.END)


ad=tk.Label(a,text="Adınız : ",bg="yellow").grid(row=0,column=0,padx=8,pady=8)
giris=tk.Entry(a).grid(row=0,column=1,padx=8,pady=8)
ad1=tk.Label(a,text="Familiya  : ",bg="yellow").grid(row=1,column=0,padx=8,pady=8)
giris1=tk.Entry(a).grid(row=1,column=1,padx=8,pady=8)
ad2=tk.Label(a,text="Yaşınız  : ",bg="yellow").grid(row=2,column=0,padx=8,pady=8)
giris2=tk.Entry(a).grid(row=2,column=1,padx=8,pady=8)
duyme=tk.Button(a,text="Qeydiyyat",command=yaddas,bg="green").grid(row=3,column=0,padx=8,pady=8)
duyme2=tk.Button(a,text="Təmizlə",command=sil,bg="red").grid(row=3,column=1,padx=8,pady=8)
# Duymeler ve girisler ve rengler olculer qrafika hazir edilir test olaraq kenarda ve yerlesdirdik

a.mainloop()  # program islek veziyyete getrilir



















