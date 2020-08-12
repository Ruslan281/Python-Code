class Mekteb:
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
        print("Mektebe yeni adam uzv oldu")

    def melumat(self):
        print("Adi ve soyadi : {0}".format(self.ad))
        print("Yasi : {0}".format(self.yas))


class Muellime(Mekteb):
    def __init__(self,ad,yas,maas):
        Mekteb.__init__(self,ad,yas)
        self.maas=maas
        print("Muellime : {0}".format(self.ad))

    def melumat(self):
        Mekteb.melumat(self)
        print("Maas : {0}".format(self.maas))

class Sagird(Mekteb):
    def __init__(self,ad,yas,sinifnomresi):
        Mekteb.__init__(self,ad,yas)
        self.sinifnomresi=sinifnomresi
        print("Sagird : {0}".format(self.ad))

    def melumat(self):
        Mekteb.melumat(self)
        print("Sinif : {0}".format(self.sinifnomresi))


# yoxlayaq yazdiqlarimizi

m=Muellime("Ruslan Huseynov",26,600)
print()
s=Sagird("Kamran Necefov",25,"11V")
print()
m.melumat()
print()
s.melumat()

        
