"""
    class:  -> Sinf

"""
class Moshina:
    def __init__(self, name, price, fast, color):
        self.name = name
        self.price = price
        self.fast = fast
        self.color = color

    def get_name(self):
        return f"Mashining nomi: {self.name}"
    

    def get_price(self):
        new_price = self.price + 10_000_000
        return f"Mashining narxi: {new_price}"
    

    def get_fast(self):
        return f"Mashining tezligi: {self.fast+10}"
    

    def get_color(self):
        a = f"Mashining Rangi: {self.color}"
        return a
    
    def info(self):
        data = """
                Mashining nomi: {self.name}
                Mashining narxi: {new_price}
                Mashining tezligi: {self.fast}
                Mashining Rangi: {self.color}
            """
        return data


damas = Moshina("Damas", 90_000_000, 180, "oq")
cobalt = Moshina("Cobalt", 100_000_000, 200, "oq")
# print(damas.get_price())
# print(damas.get_fast())

print(damas.info())
print(cobalt.info())



