from tkinter import ttk
from ttkthemes import ThemedTk  # tema reng sistemini teyin etmek

a=ThemedTk(theme="radiance")  # temani radiance olaraq teyin etdik

ttk.Label(a,text="Adiniz  :").grid(row=0,column=0)

ttk.Entry(a).grid(row=0,column=1,ipady=5,ipadx=5)

ttk.Button(a,text="Axtar").grid(row=0,column=2)

a.mainloop()
