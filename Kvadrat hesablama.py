# OOP-ye giris ve Sinif(class) tanimlanmasi

class Kvadrat:  # Sinfimizi yaradiriq
    notum="Kvadrat-butun terefleri beraber olan dordbucaqlidir."
    def k_perimetr(self,a):
        return 4*a
    def k_sahesi(self,a):
        return a*a

kv = Kvadrat()

print(Kvadrat.notum)
a=int(input("Kbadratin terefini daxil edin :"))
print("Kvadratin perimetri:",kv.k_perimetr(a))
print("Kvadratin sahesi:",kv.k_sahesi(a))
