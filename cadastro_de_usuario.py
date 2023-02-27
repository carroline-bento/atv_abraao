
import json

def salvar_banco(dados):
    dados_para_salvar = dados
    with open('cadastro.json', 'a') as arquivo:
        json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=2)
    print('Usuário cadastrado com sucesso')

def cadastrar(nome, senha):
    dados = {'Nome': nome,
             'Senha': senha}
    salvar_banco(dados)

def confirmar_senha(senha):
    senha_para_confirmar = input('Digite novamente sua senha: ')

    if senha == senha_para_confirmar:
        cadastrar(nome, senha)
    else:
        print('Não foi possível realizar o cadastro')

print('Digite seus dados para cadastro')

nome = input('Digite seu nome de usuário: ')
senha = input('Crie sua senha: ')

confirmar_senha(senha)