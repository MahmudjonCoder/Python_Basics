""" print()
    type()
    input()

    str
    int  2,3,5,6,7,33
    float 23.4 1.3
    boolean
"""

""" List

append  -> qushadi
clear  -> tozalaydi
copy  -> copy
count -> sanaydi
extend -> qushadi
index  -> index buyicha oladi
insert  -> qushadi joy
pop  -> sugurib oladi
remove -> uchiradu
reverse -> teskari
sort -> tartiblash
 
 """

#     0      1    2    3     4     5
l1 = [22, 2, 234, 34, 90, 22]
l1.append("coffee")
l1.clear()
l2 = l1.copy()
a = l1.count(22)
l1.extend(["aa", 222, False])
print(l1)
a = l1.index(True)
l1.insert(0, 1)
matn = l1.pop(4)
l1.remove("str")
print(l1)
l1.reverse()
l1.sort()
print(l1)
print(matn)

# l1 = [1, 2, 3]
# l2 = ['a', 'c', 'b']# [1,2,a,b,c,3]
# l3 = l1 + l2
# a = l1[0:2]
# c = l1[-1]                                 ']'''' [1,2,a,b,3,c,4,6,78,d, 9, f, e]
# l3 = a + l2
# l3.append(l1[-1])
# print(l3)
# l3.sort()
# print(l3)

# print(l1)
# print(type(l1))
#
# for i in dir(list):
#     if not i.startswith("__"):
#         print(i)


"""
1-masala: 
    1: bush list yaratsiz
    2: karochi faqat appendan foydalanib 15 ta dust qushasiz

2- ruyxatni tozalaysiz: ruyxat ichida 4 bta element bulsin

3 - append, insert, va extend 3 ta sidan foydalanib lubboy ruyxat yaratasiz ichoda 15 ta narsa bulsin

4- pop va removeda foydalanib qandaydir masala ishlang


5 - sort va reverse foydalanib sonlardan va str dan iborat ruyxat yarating va quydagi sort funksiyasidan foydalaning


6- ikkita listni bir biriga qushing

7:
l1 = [1,2,3,4,6,78,9]
l2 = [a, b, c, d, f, e]
natija  = [1,2,a,b,3,c,4,6,78,d, 9, f, e]

list = -> sum, max, min
"""
# ona_bank = 200_000
# ona = []
# summa = []
# ona.append("non")
# summa.append(3000)
# ona.append("tuz")
# summa.append(4000)
# ona.append("yog")
# summa.append(20_000)
# ona.append("gush")
# summa.append(80_000)
#
#
# ona.append("banana")
# summa.append(
#     25_000
# )
# opshi_summa = sum(summa)
# s = ona_bank - opshi_summa
# info = f"Onam menga aytgan ruyxatlar bu {ona}"
# info2 = f"Onam menga aytgan ruyxatlar summalari {opshi_summa}"
# q = f"qolgan summa {s}"
#
#
# print(info)
# print(info2)
# print(s)
#
# print(200_000-107_000-25_000)
















