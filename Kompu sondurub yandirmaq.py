from tkinter import * # butun paketi import edirik
import os # os modulu sisteme mudaxile ucun import edirik

ekran=Tk() # tkinteri deyiskene atadiq

ekran.title("Kompyuteri sondurmek ve Yandirmaq") # Programin adini daxil etdik
win.geometry("290x70") # Olculerini teyin eledik
win.resizable(False,False) # Olculerle oynama olmasin deye sabit saxladiq

def sondurmek(): #Sondurmek funksiyasini yaradiriq
    os.system("shutdown /s /t 1")  # Os modulunun sistem funksiyasindan istifade ederek funksiyani teyin dirik

def yeniden_baslat():
    os.system("shutdown /r /t 1") # Burda da hemcini eyniyle  (/r) den basqa

duyme1=Button(ekran,text="Söndürmək",command=sondurmek,height=3,width=17)
duyme1.grid(row=0,column=0)  # padx ve pady teyin etmedim (x ve y kimide yaza bilerik)

duyme2=Button(ekran,text="Yenidən Başlat",command=yeniden_baslat,height=3,width=17)
duyme2.grid(row=0,column=1)  # padx ve pady teyin etmedim (x ve y kimide yaza bilerik)


ekran.mainloop()  # Ekrani islek veziyyete getririk
