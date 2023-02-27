from jogos import Jogo

class JogoDaAdivinhacao(Jogo):
    def __init__(self, nome, palavras):
        super().__init__(nome, palavras)
        self.salvar_palavras()
        self.pegar_palavras()
        self.escolher_palavra()
        self.tentativas = 0
        self.acertou = False

    def verificacao(self, palavra):
        self.tentativas += 1
        if palavra == self.palavra_escolhida:
            print('Muito bem, você acertou!!!')
            print('A palavra era:', self.palavra_escolhida)
            print(f'Você conseguiu em {self.tentativas} tentativas')
            self.acertou = True
        else:
            print('Essa não é a palavra, tente novamente >_<')


lista_de_palavras = ['camelo', 'luz', 'mochila', 'escrita', 'batata', 'cenoura', 'manga']

jogo_ad = JogoDaAdivinhacao('Adivinhação', lista_de_palavras)

palavra_digitada = ''

print('##### Jogo da adivinhação #####')
print('Esse é o jogo da adivinhação, eu estou pensando em uma palavra e você terá de adivinhar')
print('Uma diquinha sobre a palavra: ')
print(f'Ela tem {len(jogo_ad.palavra_escolhida)} letras :3')

while palavra_digitada != jogo_ad.palavra_escolhida:

    palavra_digitada = input('Digite uma palavra: ').lower()
    jogo_ad.verificacao(palavra_digitada)