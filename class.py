from datetime import date
class automovel:
    def __init__(self, roda, marca):
      self.roda = roda
      self.marca = marca

class carro(automovel):
    def __init__(self,roda,marca,combustivel):
      self.combustivel = combustivel
      super().__init__(roda,marca)


car1 = carro(4, "chevrolet", "gasolina")
print("Seu carro é da marca: ",car1.marca)
print(f"Seu carro tem {car1.roda} rodas")
print("Seu carro usa o combustivel: ",car1.combustivel)

print(date.today())
data = date(2024,9, 9)
print(data)