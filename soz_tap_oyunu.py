print("Azerbaycanca sozlerin Ingilisce qarsiligi")
sozler={"kitab":"book",
        "kompyuter":"computer",
        "proqramlama":"programming",
        "stol":"table",
        "qelem":"pen"}

def axtar(soz):
    xeta="{} sozu sozler icerisinde yoxdur!"
    print(sozler.get(soz,xeta.format(soz)))

def elave(soz,mena):
    mesaj="{} sozu sozler icerisine elave edildi!"
    sozler[soz]=mena
    print(mesaj.format(soz))
def sil(soz):
    try:
        sozler.pop(soz)

    except KeyError as err:
        print(err, "sozu tapilmadi !")

    else:
        print("{} sozu sozler arasindan silindi !".format(soz))




print("1. Sozlerede soz axtar")
print("2. Sozlere soz elave et")
print("3. Sozlerden soz sil ")
no=input("Yerine yetirmek istediyiniz emeliyyati girin  : ")
if no=="1":
    soz=input("Axtardiginiz sozu daxil edin  : ")
    axtar(soz)

elif no=="2":
    soz=input("Elave edeceyiniz sozu daxil edin  : ")
    mena=input("Elave edeceyiniz sozun menasini daxil edin  : ")
    elave(soz,mena)

elif no=="3":
    soz=input("Sileceyiniz sozu daxil edin  : ")
    sil(soz)

else:
    print("Proqramdan duzgun istifade edin")

    
    
          







