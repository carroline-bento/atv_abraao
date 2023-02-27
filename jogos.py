
import json
import random

class Jogo:
    def __init__(self, nome, palavras):
        self.nome = nome
        self.palavras = palavras
        self.caminho = 'palavras_salvas.txt'
        self.palavras_salvas = []
        self.palavra_escolhida = ''
    
    def salvar_palavras(self):
        with open(self.caminho, 'w') as arquivo:
            json.dump(self.palavras, arquivo, ensure_ascii=False, indent=2)
            
    def pegar_palavras(self):
        print(f'Jogo selecionado: {self.nome}')
        with open(self.caminho, 'r') as arquivo:
            self.palavras_salvas = json.load(arquivo)

    def escolher_palavra(self):
        self.palavra_escolhida = random.choice(self.palavras_salvas)