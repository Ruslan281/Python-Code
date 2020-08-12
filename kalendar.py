from tkinter import *  # tkinter modulunu import edirik
import calendar  # import kalendar 

kale=Tk()  # tkinteri deyiskene atiriq tanimlamaq ucun
kale.title("Kalendar")  # program ad daxil edirik

def text():
    aylar_setir=month.get()
    iller_setir=year.get()
    aylar_int=int(month_str)
    iller_int=int(year_str)
    kalendar=calendar.month(iller_int,aylar_int)
    melumat.delete(0.0,END)  #Silmek ucun
    melumat.insert(insert,cal) # insert edirik


ay=Label(kale,text="Ay  : ") # Ay labeli elave edirik
ay.grid(row=0,column=0)  # Geometry
aylar_s=Spinbox(kale,from_=1,to=12,width=5)
aylar_s.grid(row=1,column=0)

il=Label(kale,text="il  : ")
il.grid(row=0,column=1)
iller_s=Spinbox(kale,from_=1700,to=2100,width=12)
iller_s.grid(row=1,column=1,padx=8)

button=Button(kale,text="Duzelt",command=text)
button.grid(row=1,column=2)

melumat=Text(kale,height=10,width=25,foreground="red")
melumat.grid(row=3,columnspan=3)

kale.mainloop()
