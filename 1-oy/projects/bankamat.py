from termcolor import cprint

cprint("\t\t Bankamat \n", "light_blue")
bank=True

parol = 2222
bank_shot = 1000_000

print("Kartangizni kiriting hurmatli mijoz:")
password = int(input("parolingzini kiriting: "))

if parol == password:
    info = """
Parol Tugri quydagi ammalrdan birini tanlang:
    1. Banalsni Kurish
    2. Pulchiqarish
    3. Orqaga qaytish
"""
    cprint(info, 'green')
    tanlov = int(input("1, 2 yoki 3  kiriting:"))
    if tanlov == 1:
        cprint(f"Banasingiz: {bank_shot}", "green")
    elif tanlov == 2:
         chiqim = int(input("qancha pul yechmoqchisiz? "))
         if 0 < chiqim <= bank_shot:
            bln = bank_shot - chiqim
            cprint(f"Siz Kartangizdan {chiqim} sum chiqardingiz: Qoldiq {bln} sum", 'green')
         else:
            cprint("Balansda buncha pul yuq", "red")
    elif tanlov == 3:
        cprint("Dastur tugadi", 'red')
    else:
        cprint("xato tanlov", "red")
else:
    cprint("Parol xato", 'red')

 

