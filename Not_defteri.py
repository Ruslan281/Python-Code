# Internet resurslarinin arasdirmalarin komekliyi ile yazilib


from tkinter import *  # Tkinteri impor edirik
from tkinter.filedialog import askopenfile,asksaveasfilename # Ayriliqda olaraq fayllari yazdiqdan sonra tkinterin fayllari acmaq ve yadda saxlamaq ucun funksiyasindan istifade edirik

pencere=Tk()  # Deyiskeni tanimlayiriq pencere olaraq
pencere.title("Not Dəftəri")  # Programa ad qoyuruq

def acmaq():   # Fayli acmaq ucun funksiya teyin edirik
    blank.delete("1.0",END)  # Silmek ucun
    file=askopenfile(mode="r",filetypes=[("text files","*.txt")])
    if file is not None:
        text=file.read()
        blank.insert("1.0",text)

def yadda_saxla():
    notepad_text=blank.get("1.0","end-1c")
    file=asksaveasfilename(title="Save",filetypes=[("text files","*.txt")])
    with open(file,"w") as data:
        data.write(notepad_text)


menubar=Menu(pencere)
pencere.config(menu=menubar)

menyular=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fayllar",menu=menyular)
menyular.add_command(label="Aç",command=acmaq)
menyular.add_command(label="Saxla",command=yadda_saxla)
menyular.add_command(label="Çıxış",command=pencere.destroy)
blank=Text(pencere,font=("arail",10))
blank.pack() # Tanimlayiriq geriye dondurmek
pencere.mainloop()  # Programi islek veziyyete getririk















