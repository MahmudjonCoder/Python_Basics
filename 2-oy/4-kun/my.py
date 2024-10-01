class Hayvon:
    def __init__(self, ism, yosh, rangi, kg):
        self.ism=ism
        self.yosh=yosh
        self.rangi=rangi
        self.kg=kg

    def get_ism(self):
        return f"hayvonning ism{self.ism}"
    
    def get_yosh(self):
        new_yosh = self.yosh + 200
        return f"hayvonning yosh{new_yosh}"

    def get_rangi(self):
        return f"hayvonning rangi{self.rangi}"

    def get_kg(self):
        new_kg = self.kg + 200
        return f"hayvonning kg{new_kg}"



sher= Hayvon("sher", 12, "toq sariq", 500 )
print(sher.get_ism())
print(sher.get_rangi())
print(sher.get_kg())
print(sher.get_yosh())
