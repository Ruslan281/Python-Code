class Rus():
    eded=0
    def __init__(self,ad,vezife):
        self.ad=ad
        self.vezife=vezife

        print("{0}  {1} vezifesine qebul edildi".format(self.ad,self.vezife))

        Rus.eded+=1


        r1=Rus("Ruslan Huseynov","Developer")
        print("Iscilerin sayi : {0}".format(Rus.eded))
        r2=Rus("Kamran Necefov","Komekci")
        print("Iscilerin sayi : {0}".format(Rus.eded))
        print()
        print("Idarede vezifeler :")
        print(r1.vezife)
        print(r2.vezife)
        print()
        print("Iscilerin adlari :")
        print(r1.ad)
        print(r2.ad)
    
