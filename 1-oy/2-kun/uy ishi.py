str = "mening ismim maxmudjon"  #birinch sozdagi birinchi harifni kotta qilib beradi
print(str.capitalize())

str = "Mening ismiM maXMudjon"  #matindagi kotta harflarni kichik qilib beradi
print(str.casefold())

str = "SALOM"
print(str.center(10, "#"))

str = "Mening ismim Maxmudjon.Maxmudjon yaxshi bola "  #matinda nechta birxil soz borligini hisoblab beradi
print(str.count("Maxmudjon "))

str = "bu birinchi matn . bu sekund matin"
print(str.find("matin"))

str = "bu birinchi matn . bu sekund matin2"
print(str.endswith("matin2"))

str = "m\ta\tx\tm\tu\td\tj\to\tn"  #
print(str.expandtabs(2))

str = "bu birinch matn"
print(str.index("i"))

str = "maxmudjon007"
print(str.isalnum())

str = "tomCruise"
print(str.isalpha())

str = "46"
print(str.isdecimal())

str = "45453"
print(str.isdigit())

str = "maxmudjon777"
print(str.isidentifier())

str = "mening ismi maxmudjon"
print(str.islower())

str = "35446"
print(str.isnumeric())

str = "sylvester"
print(str.isprintable())

str = "  "
print(str.isspace())

str = "Maxmudjon"
print(str.istitle())

str = "SUPER MARKET"
print(str.isupper())

str = {"maxmudjon", "maxmudov", "bahrom", "rasuljon"}
sep = "++"
print(sep.join(str))

str = "MaxMudjon"
print(str.lower())

str = "$$$$$$-PUL"
print(str.lstrip("$-"))

str = "salom men aqilli bolaman , va aqilli man"
print(str.replace("aqilli", "bilagon"))

str = "salom men aqilli bolaman , va aqilli man"
print(str.rfind("aqilli"))

str = "salom men aqilli bolaman , va aqilli man va zo'r aqilli man"
print(str.rindex("aqilli"))

str = "America Vandel"
print(str.rjust(25, "A"))

str = "futbol, koptok, samalyot, vertalyot "
print(str.rsplit(",", 3))

str = "mening ismim Mamxudjon###########"
print(str.rstrip("#"))

str = "mening@@@@@@@@@@@@@@@@@@@@ismim@@@@@@@Mamxudjon"
print(str.split("@", 1))

str = "mening\n\n\n\n\n\nismim\n\n\n\nMamxudjon"
print(str.splitlines(False))

str = "salom men aqilli bolaman.va bilagon bolaman"
print(str.startswith("s"))

str = "salom men aqilli bolaman.va bilagon bolaman"
print(str.swapcase())

str = "mening ismim maxmudjon"
print(str.title())

str = "Salom yaxshimisiz"
print(str.upper())

str = "Wow"
print(str.zfill(15))

ism = str
familiya = input("family kiriting ")
yosh = str
print(ism)
print(familiya)
print(yosh)
info = f"Assalomu Alaykum sizning ismingiz{ism}, familiyangiz {familiya}, yoshingiz{yosh} yosh"
print(info)
