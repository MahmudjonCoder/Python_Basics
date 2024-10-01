# k = int(input("Enter k: "))
# n = int(input("Enter n: "))
#
# natija = ""
# for i in range(n):
#     natija += str(k)
#
# print(natija)
import sys

# son =0
# son2 =0
# numbers_a =(13,25,37,49,50)
# numbers_b= (12,24,36,48,49)
# for i in numbers_a:
#     son+=i
# for i in numbers_b:
#     son2+=i
# print(son+son2)

# son =0
# son2 =0
# numbers_a =(13,25,37,49,50)
# numbers_b= (12,24,36,48,49)
# for i in numbers_a:
#     son-=i
# for i in numbers_b:
#     son2-=i
# print(son,son2)
# print(son-son2)

# narxi =45000
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     narxi.append(i**narxi)
# print(numbers)
# print(narxi)

# def konfet_narxi(narxi):
#
#     narxlar = {}
#     for i in range(1, 11):
#         narxlar[i] = i * narx
#     return narxlar
#
# narx = float(input("1 kg konfetning narxini kiriting: "))
#
# narxlar = konfet_narxi(narx)
#
# print("Konfet narxlari:")
# for kg, narx in narxlar.items():
#     print(f"{kg} kg: {narx} so'm")


# bir_kg_narxi = int(input("konfetning narxini kiriting: " ))
#
# for vazn in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
#     narx = vazn * bir_kg_narxi
#     print(f"{vazn} kg konfetning narxi: {narx:} so'm")
#

# bir_kg_narxi = int(input("konfetning narxini kiriting: "))
#
# for vazn in [1.2, 1.4, 1.6, 1.8, 2]:
#     narx = vazn * bir_kg_narxi
#     print(f"{vazn} kg konfetning narxi: {narx:} so'm")


# a = 1
# b = 10
#
# yigindi = sum(range(a, b+1))
#
# print(f"{a} dan {b} gacha bo'lgan barcha butun sonlar yig'indisi: {yigindi}")


# def butun_sonlar_kopaytmasi(a, b):
#     kopaytma = 1
#     for son in range(a, b + 1):
#         kopaytma *= son
#     return kopaytma
#
# a = 1
# b = 10
# natija = butun_sonlar_kopaytmasi(a, b)
# print(f"{a} dan {b} gacha bo'lgan barcha butun sonlar ko'paytmasi {natija} ga teng")


# def butun_sonlar_kvadratlari_yigindisi(a, b):
#     yigindi = 0
#     for son in range(a, b + 1):
#         yigindi += son ** 2
#     return yigindi
#
# a = 2
# b = 2
# natija = butun_sonlar_kvadratlari_yigindisi(a, b)
# print(f"{a} dan {b} gacha bo'lgan barcha butun sonlar kvadratlari yig'indisi {natija} ga teng")


# n = int(input("n:"))
# total = 0
# for i in range(1,n+1):
#     total += 1/i
#
# print(total)
