"""
class Maktab:
    def __init__(self, maktab_nomi, manzil):
        self.maktab_nomi = maktab_nomi
        self.manzil = manzil


class Talaba(Maktab):
    def __init__(self, maktab_nomi, manzil, ism, familya, sinf=None):
        super().__init__(maktab_nomi, manzil)
        self.ism = ism
        self.familya = familya
        self.sinf = 8

    def info(self):
        data = f"Mening ism familiyam {self.familya} {self.ism} \n"
        data += f"Men {self.manzil}dagi {self.maktab_nomi}da {self.sinf}-chi sinfda uqiman"
        return data

talaba1 = Talaba("22-maktab", "Chilonzor", "Mahmudjon", "Mahmudov")
print(talaba1.info())

"""

class Reastoran:
    def __init__(self,nomi, manzili ):
        self.nomi =nomi
        self.manzili = manzili


class Odam(Reastoran):
    def __init__(self, nomi, manzili,nima_ovqatlari, narxi ):
        super().__init__(nomi, manzili)    # superga etibor berasiz
        self.nima_ovqatlari =nima_ovqatlari
        self.narxi =narxi

    def info(self):
        data = f"Restoranning nomi {self.nomi} va manzili {self.manzili} va ovqat {self.nima_ovqatlari} narxi {self.narxi}"
        return data

odam1 = Odam("strit","chinolzor", "lavash", 40000 )
print(odam1.info())

