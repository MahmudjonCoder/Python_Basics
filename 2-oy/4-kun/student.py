class Kitob:
    def __init__(self, kitob_nomi, narxi,nech_betligi,nima_xaqidaligi ):
        self.kitob_nomi=kitob_nomi
        self.narxi=narxi
        self.nech_betligi=nech_betligi
        self.nima_xaqidaligi=nima_xaqidaligi

    def get_nomi(self):
        return f"kitob_nomi{self.kitob_nomi}"
    def get_narxi(self):
        return f"narxi{self.narxi}"
    def get_nech_betligi(self):
        return f"nech_betligi{self.nech_betligi}"
    def get_nima_xaqidaligi(self):
        return f"nima_xaqidaligi{self.nima_xaqidaligi}"

    def info(self):
        data = """
             kitob_nomi: {self.kitob_nomi}
             narxi: {self.narxi}
             nech_betligi: {self.nech_betligi}
             nima_xaqidaligi: {self.nima_xaqidaligi}
        """
        return data
    
sariq_devni_minib=Kitob("sariq_devni_minib", 100_000, 500, "bu kiob juda qaziqarli ")    
alpomish = Kitob("alpomish", 111_000, 500, "bu kiob juda qaziqarli")    

print(sariq_devni_minib.info())
print(alpomish.info())







