""" 1
    arifmetik ammalrni keltirib uting qushish, ayrish, daraja, qoldiq
    int va floatga izoh yozing
"""
# son= 20
# son2=30
# qoshish3= son + son2
# print(qoshish3)

# ayrish= 1000
# ayrish2=234
# ayrish3 =ayrish - ayrish2
# print(ayrish3)

# daraja= 2345
# daraja2= 455
# daraja3=daraja**daraja2
# print(daraja3)

# qoldiq=20
# qoldiq2=3
# qoldiq3=qoldiq%qoldiq2
# print(qoldiq3)

#int= faqat butun son oladi
#float= butun va qoldiqli son oladi

""" 2
    boolean nima fa booleanga doir 4 ta masala
"""
# son=(123456==2345 and 234556<10 and 12345678<78) 
# print(son)

# son2=(123456<2342345 and 234556<10 or 12345678>78) 
# print(son2)

# son3=(123456>234545678 or 234556==10 or 12345678<78) 
# print(son3)

# son4=(12345<2345 or 234556<10 and 12345678!=78) 
# print(son3)

#booleanga >, <, =>, =<, !=, ==

""" 3
    string (nima) methodlarini yozib bering har biriga tarif ham bering kamida 4 ta method yozing
    kesma nima?  1 ta misol
"""
# ism= "maxmudov maxmudjon baxrom o'g'li"
# kotta =ism.upper()
# kichik=ism.lower()
# bosh_harfni_kotta_qilish= ism.title()
# b= ism.capitalize()

# print (kotta)
# print (kichik)
# print (bosh_harfni_kotta_qilish)
# print (b)

""" 4
    list (nima) methodlarini yozib bering har biriga tarif ham bering kamida 4 ta method yozing
"""
# l1=["olma", "banan", "uzum", "gilos"]

# l1.append("salom")
# l1.clear()
# a = l1.pop(1)
# l1.copy()
# print(l1)
# print(l1)
# print(l1)
# print(l1)
# print(a)

#biz list ichiga hamma narsa berak boladi, listga qoshib, ochirish,sugurub olish va yana boshqa narsa berak boladi.
""" 5
    tuple (nima) methodlarini yozib bering har biriga tarif ham bering kamida 4 ta method yozing
"""
# ism = ("maxmudjon", "slom", "avazbek", "kompuyuter","maxmudjon")
# a = ism.count("maxmudjon")
# b = ism.index("avzbek")
# c= ism.__len__()
# print(c)
# print(b)


""" 6
    shart operatorlarini yozib izoh yozing va masala:
        hafta kunini kiritaman menga kunni chiqarib bersin:
            masalan: 1 kiritsam Dushanba
            agar 8 kiritsam bunday hafta kunoi yuq deb chiqarsi
"""
# while True:
# a = int(input("son kirit: "))
# hafta_kunlari= "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba" ,"yakshanba"
# if a == 1:
#     print(a, "dushanba".title())
# elif a == 2:
#     print(a, "seshanba".title())
# elif a == 3:
#     print(a, "chorshanba".title())
# elif a == 4:
#     print(a, "payshanba".title())
# elif a == 5:
#     print(a, "juma".title())
# elif a == 6:
#     print(a, "shanba".title())
# elif a == 7:
#     print(a, "yakshanba".title())
# else:
#     print("Bunday hafta kuni yuq")
""" 7
    for nima:
        1-10 gacha sonlari forda chiqarib bering 
        1 10 gacha sonlarni juft sonlarni chiqarib bering
# """
# for i in range(1, 11):
#     print(i)

# for i in range(1, 10): 
#     if i % 2 == 0:
#         print(i)  


""" 8
dict  nima:
    dict misol keltirng va itemas() keys() values() ishlatib chiqing
"""
# dict_uzb_ing ={
#       "matem":"math",
#       "avtobus":"bus",
#       "salom":"hello",
#       "xayr":"baybay", 
# }

# for i in dict_uzb_ing.keys():
#       print(i)

# for i in dict_uzb_ing.values():
#       print(i)

# for i in dict_uzb_ing.items():
#       print(i)