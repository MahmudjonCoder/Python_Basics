# son1 = int(input("son kiriting"))
# son2 = son1 * 4
# print(son2)


# son1 = int(input("son kiriting"))
# son2 = son1 ** 2
# print(son2)


# son1 = int(input("son kiriting"))
# son2 = int(input("son kiriting"))
# yuzasi = son1 * son2
# peremetiri = 2 * (son1+son2)
# print(son1)
# print(son2)


# diametr = int(input("son kiriting"))
# uzunlik = diametr * 3.14
# print(uzunlik)

# kub = int(input("son kiriting"))
# hajmi = kub ** 3
# sirti = 6 * (kub*2)
#
# print(hajmi)
# print(sirti)


# a = int(input("son kiriting"))
# b = int(input("son kiriting"))
# c = int(input("son kiriting"))
# hajm = a * b * c
# sirti = 2 * (a * b + b * c + a * c)
# print(hajm)
# print(sirti)

# radiusi = int(input("radiusga kiriting"))
# uzunligi = int(input("uzunligiga kiriting"))
# yuzasi = int(input("yuzasiga kiriting"))
# l = 2 * uzunligi * radiusi
# s = uzunligi * (radiusi * 2)
# print(l)
# print(s)


# a = int(input("son kiriting"))
# b = int(input("son kiriting"))
# arifmetk = (a + b) / 2
# print(arifmetk)

import math

#
a = int(input("son kiriting"))
b = int(input("son kiriting"))
geometrik = a * b
ildiz = math.sqrt(geometrik)
print(geometrik)
print(ildiz)

# a = int(input("son kiriting"))
# b = int(input("son kiriting"))
# yigindisi = a + b
# kopaytmasi = a * b
# kvadrat = a ** b
# print(yigindisi)
# print(kopaytmasi)
# print(kvadrat)



# metir = 100
# sm = int(input("sm kiriting"))
# natija = sm / metir
# print(natija)
#
# tonna = 1000
# kg = int(input("kg kirit: "))
# natija = kg / tonna
# print(natija)
#
# kb = 1024
# bayt = int(input("bayt  kirit: "))
# natija = bayt / kb
# print(natija)
#
# a = int(input("son kirit: "))
# b = int(input("son kirit: "))
# natija = b - a
# print(natija)

# a = int(input("son kirit: "))
# b = int(input("son kirit: "))
# natija = b - a
# print(f"joylashmagan qismi{natija}")

# son = int(input("son kiriting"))
# onlik = son // 10
# birlik = son % 10
# print(onlik)
# print(birlik)
# print(f"o'nliklar honasidagi raqam {onlik} bilrliklar xonasidagi raqam {birlik}")

# son = int(input("son kiriting"))
# son2 = son // 10
# son3 = son % 10
# yegindi = son2 + son3
# print(yegindi)

# son = int(input("son kiriting"))
# unlik = son // 10
# birlik = son % 10
# print(unlik)
# print(birlik)
#
# a = (birlik * 10) + unlik
# print(a)

# son = int(input("son kiriting"))
# son2 = son // 100
# print(son2)

# son = int(input("son kiriting"))
# son2 = son % 10
# son3 = son // 10
# print(f"birlik {son2}")
# print(f"onlik {son3}")
#
# son = int(input("son kiriting"))
# son2 = son % 10
# son3 = son // 10
# son4 = son // 100
# print(son2 + son3 + son4)

son = int(input("son kiriting"))
onlik = son % 10
birlik = son / 10
yuzlik = son // 100
print(onlik)
print(birlik)
print(yuzlik)
a = (onlik * 100) + (birlik * 10) + yuzlik
