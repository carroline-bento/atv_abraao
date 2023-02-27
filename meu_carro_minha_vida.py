class Carro:
    def __init__(self, nome, consumo, qtd_combustivel=0):
        self.nome = nome 
        self.consumo = consumo # km/L
        self.qtd_combustivel = qtd_combustivel
        self.contador_consumo = 0 # marca os km percorridos com 1L
        self.distancia_percorrida = 0

    def andar(self, distancia):
        while self.distancia_percorrida < distancia:
            print(f'{self.nome} está andando...')
            self.distancia_percorrida += 1
            self.contador_consumo += 1
            # print(f'Distância percorrida: {self.distancia_percorrida}')

            if self.contador_consumo % self.consumo == 0:
                self.qtd_combustivel -= 1 
                print(f'Distância percorrida: {self.distancia_percorrida}')
                print('- 1L de combustível')


    def obterGasolina(self):
        return self.qtd_combustivel
    
    def adicionarGasolina(self, quantidade):
        self.qtd_combustivel += quantidade
        

# c1 = Carro('Fusca', 8, 40)
# print(c1.obterGasolina())
# c1.andar(40)
# print(c1.obterGasolina())
# c1.adicionarGasolina(10)
# print(c1.obterGasolina())
# c1.andar(200)
# print(c1.obterGasolina())

c2 = Carro('Gol', 3, 30)
print(c2.obterGasolina())
c2.andar(40)
print(c2.obterGasolina())
c2.adicionarGasolina(10)
print(c2.obterGasolina())
c2.andar(60)
print(c2.obterGasolina())