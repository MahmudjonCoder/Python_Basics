class Car:
    def __init__(self, nomi, model, yili, tezligi):
        self.nomi = nomi
        self.model = model
        self.yili = yili
        self.tezligi = tezligi

    def avtomobil(self):
        return f"Assalomu Alaykum bu mening mashinam {self.nomi}"

    def get_nomi(self):
        return f"nomi: {self.nomi}"

    def get_model(self):
        return f"model: {self.model}"

    def get_yili(self):
        return f"yili: {self.yili}"

    def get_tezligi(self):
        return f"tezligi: {self.tezligi}"



mashina1 = Car('Ling_bao_box', 'Ling_box', 2024, 300)
mashina2 = Car('Tahoya', 'Taho', 2024, 330)
print(mashina1.avtomobil())
print(mashina1.get_nomi())
print(mashina1.get_model())
print(mashina1.get_yili())
print(mashina1.get_tezligi())
print(mashina2.avtomobil())
print(mashina2.get_nomi())
print(mashina2.get_model())
print(mashina2.get_yili())
print(mashina2.get_tezligi())




