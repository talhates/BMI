Kilo= float(input("Kilonuzu giriniz: "))
Boy= float(input("Boyunuzu giriniz: {metre cinsi olarak ---1.75...} "))
BMI= (Kilo / Boy **2)
if BMI <=18.5 :
    print("BMI değeriniz: Zayıf")
elif BMI <=25 :
    print("BMI değeriniz: Normal")
elif BMI <=30 :
    print("BMI değeriniz: Kilolu")
else:
    print("BMI değeriniz: Obez")