from termcolor import cprint  # rangli chiqarish uchun

# print("\t\tHafta Kunlari\n")
# shart = True
# while shart:
#     kun = int(input("haft kunini kiriting (1-7) butun sonlarda: "))
#     if 1 <= kun < 8:
#         if kun == 1:
#             cprint("Dushanba", "green")
#         elif kun == 2:
#             cprint("Seshanba", "green")
#         elif kun == 3:
#             cprint("Chorshanba", "green")
#         elif kun == 4:
#             cprint("Payshanba", "green")
#         elif kun == 5:
#             cprint("Juma", "green")
#         elif kun == 6:
#             cprint("Shanba", "green")
#         elif kun == 7:
#             cprint("Yakshanba", "green")
#     else:
#         cprint("Bunday hafta kuni mavjud emas", "red")
#     davom = input("davom eishni xohlaysizmi (yes/no)").lower()  # Yes  -> yes
#     if davom == "yes":
#         continue
#     elif davom == "no":
#         shart = False
#     else:
#         cprint("Xato narsa kiritingiz va dastur tugadi", "red")
#         shart = False

         

# cprint("Dastur tugadi")





print("\t\tOylar\n")
shart = True
while shart:
    kun = int(input("OYlarni kiriting (1-12) butun sonlarda: "))
    if 1 <= kun < 13:
        if kun == 1:
            cprint("Yanvar", "green")
        elif kun == 2:
            cprint("Fevral", "green")
        elif kun == 3:
            cprint("Mart", "green")
        elif kun == 4:
            cprint("Maprel", "green")
        elif kun == 5:
            cprint("May", "green")
        elif kun == 6:
            cprint("Iyun", "green")
        elif kun == 7:
            cprint("Iyul", "green")
        elif kun == 8:
            cprint("Avgust", "green")
        elif kun == 9:
            cprint("Sentabr", "green")
        elif kun == 10:
            cprint("Oktabr", "green")
        elif kun == 11:
            cprint("Noyabr", "green")
        elif kun == 12:
            cprint("Dekabr", "green")    
    else:
        cprint("Bunday oy mavjud emas", "red")
    davom = input("davom eishni xohlaysizmi (yes/no)").lower()  
    if davom == "yes":
        continue
    elif davom == "no":
        shart = False
    else:
        cprint("Xato narsa kiritingiz va dastur tugadi", "red")
        shart = False

         

cprint("Dastur tugadi")



