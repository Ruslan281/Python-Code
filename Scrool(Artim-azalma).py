# bu yazilim oyrenmek meqsedile yazilib ve arasdirilib


from tkinter import *  # import tkinter edirik

def secmek():
    deyer="Value= " + str(v.get())
    giris.config(text=deyer)

b=Tk()  
b.geometry("200x100")
v=IntVar()  # Int formatinda yerlesdiririk
yum=Scale(b,variable=v,from_=1,to=50,
            orient=HORIZONTAL)

yum.pack(anchor=CENTER)

duyme=Button(b,text="Value",command=secmek)
duyme.pack(anchor=CENTER)  # Merkezlesdirmek

giris=Label(b)
giris.pack()
b.mainloop()

