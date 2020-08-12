import matplotlib.pyplot as plt  # Qrafikani hazirlamaq ucun import edirik

melumatlar="ITMIM","EMDK","Diger","Developer"  # Hansi sahelere aid edeceyikse elave edirik hemin saheleri
fazileri=[45,42,3,30]  # Hansi saheden nece faiz olacaqini qeyd etmek ucun rqemleri daxil edirik

reng=["gold","yellowgreen","lightcoral","lightskyblue"]  # reng sistemi tkinterden gotrulub  reng sisteminide istedityimiz kimi teyin edirik

plt.pie(fazileri,labels=melumatlar,colors=reng,autopct="% 1.1f  %%",shadow=True,startangle=140)

plt.show()  # Programi islek veziyyete getirmek ucun Matplotlibin Pyplotdan istifade edirik
