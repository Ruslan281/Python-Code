# Bu programin qrafik arauzu test edilib islenib
# Bu programda istifade edilen reng tonlari asagidaki linde var
#  http://www.tcl.tk/man/tcl8.3/TkCmd/colors.htm    (Reng_novleri)





import tkinter as tk
from tkinter import *
# tkinteri import edek
from datetime import datetime as vaxt
# Vaxt modulunu daxil etdik
from tkinter import filedialog,messagebox
# Elave olaraq qarismasin deye tkinterin messagebox funksiyasini elave etdik



def Fayllama():
    FaylinAdi=Label(rus,text="Faylin Adi  : ",font=("",15,"bold"),bg="green").grid(row=0,column=0,padx=5,pady=5)
    #Faylin adi deye basliq yaratdiq (Label)

    FalinAdiGiris=Entry(rus,width=50,textvariable=fileName,bg="darkgrey").grid(row=0,column=1,padx=5,pady=5)

    DaxilEt=Button(rus,text="Daxil et",width=20,command=fileNovu,highlightbackground="yellow").grid(row=0,column=2,padx=5,pady=5)
    # Daxil et butonunu hazirladiq

    MetinYazmaq=Label(rus,text="Yazacaqiniz Metin  : ",font=("",15,"bold"),bg="green").grid(row=1,column=0,padx=5,pady=5)
    
    rus.FaylGiris=Text(rus,width=120,height=30,bg="darkgrey").grid(row=2,column=0,columnspan=3,padx=5,pady=5)
    # Metni yazacaqimiz yerleri teyin eledik

    Temizle=Button(rus,text="Metni Temizle",width=20,command=textSil,highlightbackground="red").grid(row=3,column=0,padx=5,pady=5)
    # Bundan elave olaraq sehv yazilmis sozleri silmek ucun Metni temizle deye bir utonda elave eledik

    YaddaSaxla=Button(rus,text="Yaddasda Saxla",width=20,command=fileYazaq,highlightbackground="green").grid(row=3,column=2,padx=5,pady=5)
    #Yazilmis metni yadda saxlamaq ucun Button))
def fileNovu():
    f_name=filedialog.asksaveasfilename(initialdir=r"C:\Users\KTB\Desktop",filetypes=(("Text File(*.txt)","*.txt"),("DOC File(*.doc)","*.doc"),("All File")))
    fileName.set(f_name)

# Yaratdigimiz bu funksiyada yazdigimiz metni yaddasa vererken ferqli uzantilari secmek ucun bir nece fayl uzantisi elave eledik
def textSil():
    rus.FaylGiris.delete("1.0",END)
#Silmek ucun bu funksiyani teyin eledik
def fileYazaq():
    file_name_path=fileName.get()
    if len(file_name_path)!=0:
        with open(file_name_path,"w") as fileOpen:             # Internet uzerinden komeklik aldim
            fileContent=rus.fileTextEntry.get("1.0",END)
            fileOpen.write(fileContent)
            messagebox.showinfo("Yaddasda saxla","Fayl yaddasda saxlanildi")
    else:
        default_path=r"C:\Users\KTB\Desktop"
        default_filename=default_path+str(dt.now().strftime("%d%m%Y %H%M"))+".txt"  # hemcinin burda

        with open(default_filename,"w") as fileOpen: # Fayl sistemini acdiq
            fileContent=root.FaylGiris.get("1.0",END)
            fileOpen.write(fileContent)
            messagebox.showinfo("Yaddasda saxla","Yadda saxlanildi")

rus=tk.Tk()
rus.title("Metin Cevirme") # Adini daxil etdik(title)
rus.geometry("1200x900") # Olculerini daxil etmek(geometry)
rus.resizable(False,False) # Ekran olculerinde deyisiklik edilmesin (0,0)
rus.configure(background="green") # arxa gorunusu(backgroundu)
fileName=StringVar() # Yazi tipi
Fayllama() # Funksiyani cagirdiq
rus.mainloop() # Programin qrafik ara uzunu islek veziyyete getirmek










    
