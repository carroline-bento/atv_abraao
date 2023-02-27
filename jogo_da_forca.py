from jogos import Jogo

class JogoDaForca(Jogo):
    def __init__(self, nome, palavras):
        super().__init__(nome, palavras)
        self.salvar_palavras()
        self.pegar_palavras()
        self.escolher_palavra()
        self.tentativas = 0
        self.letras_acertadas = ''
        self.ganhou = False

    def verificar_letra(self, letra):
        self.tentativas += 1
        # print(self.palavra_escolhida)
        if letra in self.palavra_escolhida:
            self.letras_acertadas += letra  
            self.modificar_palavra_formada()

        else:
            print('Essa letra não está na palavra secreta')
    
    def modificar_palavra_formada(self):
        self.palavra_formada = ''
        for letra in self.palavra_escolhida:
            if (letra in self.letras_acertadas):
                self.palavra_formada += letra
            else:
                self.palavra_formada += '*'
        
        print(self.palavra_formada)
        self.verificar_ganhador(self.palavra_formada)

    def verificar_ganhador(self, palavra):
        if palavra == self.palavra_escolhida:
            print('Você acertou!!!')
            print('A palavra era ', self.palavra_escolhida)
            print('Tentativas necessárias: ', self.tentativas)
            self.ganhou = True
            return self.ganhou


    
# jogo_1 = JogoDaForca('Forca', ['paralelepípedo', 'ornitorrinco', 'mamífero', 'catavento'])
# jogo_1.salvar_palavras()
# jogo_1.pegar_palavras()
# jogo_1.escolher_palavra()
# print(jogo_1.palavra_escolhida)
# jogo_1.tornar_palavra_secreta()
# jogo_1.verificar_letra('o')
# # O replace()método substitui uma string por outra string

jogo_f = JogoDaForca('Forca', ['casa', 'queijo', 'joelho', 'caderno', 'abajur', 'harry-potter'])

print('##### Jogo da Forca #####')
print('Tente todas acertar as letras da palavra :3')

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    jogo_f.verificar_letra(letra_digitada)
    
    if jogo_f.ganhou:
        break
    

    
