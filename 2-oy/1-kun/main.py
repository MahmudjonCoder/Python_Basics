"""
Funksiyalar:
    print()
    input()
    leng()

Data
    int:  
    string: 
    boolean:  
    list:
    tuple:
    float:
    dict:
    set: 
"""
# def salom():
#     print("salom")
# salom()


# def salom(name):
#     print(f"salom {name.upper()}")
# salom("Avazbek")
# salom("Mosh")
# salom("Tim")
# salom("Santiago")


# def salom(name):
#     print(f"Salom {name.upper()}")
# salom("Bahrom")
# salom("Maxmudjon")
# salom("Rasuljon")
# salom("Abubkar")
# salom("Umar")

# def chech_password(parol: str):
#     parol2 = "2222"
#     if parol == parol2:
#         print(True)
#     else:
#         print(False)

# chech_password(2222)

# print(len("salom"))
# def uzunlik(uzunlik):
#     print(f"Uzunlik: {len(uzunlik)}")
# uzunlik("salommmmmmmm")    


# Hello Muhmud  -> kotta harflar: HM    isupper()
#               -> kichik harflar  ellouhmud   islower()



# a = "Hello Muhmud"
# kotta = ""
# kichik = ""

# for i in a:
#     if i.isupper():
#         kotta += i
#     elif i.islower():
#         kichik += i
#     else:
#         pass
# print(kotta)
# print(kichik)


# def kotta_kichik_sonlar(a):
#     kotta = ""
#     kichik = ""
#     sonlar = ""
#     for i in a:
#         if i.isupper():
#             kotta += i
#         elif i.islower():
#             kichik += i
#         else:
#             pass
#     print(kotta)
#     print(kichik)

# kotta_kichik_sonlar("Salom World")     


# for i in dir(str):
#     if i.startswith("__"):
#         pass
#     else:
#         print(i)

# tel = "+99899410487"

# if tel.startswith("+") and len(tel) == 13 and tel[1:].isdigit():
#     print(True)
# else:
#     print(False)

def check_card(number):
    if number.startswith("+") and len(number) == 13 and number[1:].isdigit():
        print(True)
    else:
        print(False)

user = input("Enter phone number: ")
check_card(user)



