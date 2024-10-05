""" OOP Vorislik """
"""
class Hayvon:
    def __init__(self, name, ovoz):
        self.name = name
        self.ovoz = ovoz

    def ovoz(self):
        pass


class It(Hayvon):
    def ovoz_chiqar(self):
        print( f" Itning nomi {self.name} va u {self.ovoz} ovoz chiqaradi")

class Mushuk(Hayvon):
    def ovoz_chiqar(self):
        print( f" Mushukning nomi {self.name} va u {self.ovoz} ovoz chiqaradi")

class Mol(Hayvon):
    def ovoz_chiqar(self):
        print( f" Molning nomi {self.name} va u {self.ovoz} ovoz chiqaradi")


it = It("Chorni", "vov")
mushuk = Mushuk("Tom", "miyov")
mol = Mol("Sen Molsan", "Muuuu")
it.ovoz_chiqar()
mushuk.ovoz_chiqar()
mol.ovoz_chiqar()
"""

class Moshina:
    def __init__(self, name, tezligi):
        self.name=name
        self.tezligi=tezligi

    def tez(self):
        pass


class Lingbox(Moshina):
    def tez(self):
        print( f"moshinanig nomi{self.name} unnig rangi {self.tezligi} 3000 km")

class Bugatti(Moshina):  # !
    def tez(self):
          print( f"moshinanig nomi{self.name} unnig rangi {self.tezligi} 3000 km")         

class Lambarghini(Moshina):
    def tez(self):
          print( f"moshinanig nomi{self.name} unnig rangi {self.tezligi} km")    

linbox= Lingbox("lingbox", "300")
bugatti= Bugatti("Bugatti", "400")
lambarghini=Lambarghini("Lambarghini", "350")

linbox.tez()
bugatti.tez()
lambarghini.tez()


""" Yana bita """

