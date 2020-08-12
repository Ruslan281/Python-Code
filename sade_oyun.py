import time
import random
import sys

class Oyuncu():
    def __init__(self,ad,can=5,enerji=100):
        self.ad=ad
        self.zerbe=0
        self.can=can
        self.enerji=enerji


    def movcud_veziyyet (self):
        print("zerbe :",self.zerbe)
        print("can : ",self.can)
        print("enerji : ",self.enerji)

    def hucum(self,reqib):
        print("Bir hucum yerine yetirdiniz.")
        print("Hucum davam edir.Gozleyin")

        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush= True)


        netice=self.hucum_neticesini_hesabla()

        if netice==0:
            print("\nNETICE : qazanan teref yoxdur")

        if netice==1:
            print("\nNETICE : Reqibinizi darmadagin etdiniz")
            self.darbele(reqib)
        if netice==2:
            print("\nNETICE : Reqibinizden zerbe aldiniz")
            self.darbele(self)

    def hucum_neticesini_hesabla(self):
        return random.randint(0,2)

    def qac(self):
        print("Geri cekilirem ")
        for i in range(10):
            time.sleep(0.3)
            print("\n",flush=True)
        print("Reqibiniz sizi yaxaladi")


    def darbele(self,darbelenen):
        darbelenen.zerbe+=1
        darbelenen.enerji-=1
        if darbelenen.can<1:
            darbelenen.enerji=0
            print("Oyunu {} qazandi!".format(self.ad))
            self.oyundan_cix(self)
            print("Oyundan cixilir....")
            sys.exit()


siz=Oyuncu("Ruslan")
reqib=Oyuncu("Xanim")

while True:
    print("Hal-hazirda reqibinizle qarsi qarsiyasiz.",
          "Yerine yetirmek istediyiniz hucum : ",
          "Hucum :  s",
          "Qac     :  w",
          "Cix      :   q",sep="\n")

    hamle=input("\n> ")
    if hamle=="s":
        siz.hucum(reqib)

        print("Reqibinizin Veziyyeti")
        reqib.movcud_veziyyet()

        print("Sizin veziyyetiniz")
        siz.movcud_veziyyet()

    if hamle=="w":
        siz.qac()

    if hamle=="q":
        siz.oyundan_cix()
        
    







            
    
