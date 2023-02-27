# ESSE ARQUIVO PRECISA DO ARQUIVO requirements.txt

from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from scipy.integrate import quad
from tkinter import *


def derivada():
    try:
        x = symbols('x') # Declara uma variável independente 
        func_escrita = funcao.get()
        expr = parse_expr(func_escrita)
        derivada = diff(expr,x)
        marcador.configure(text=derivada)
        marcador2.configure(text="")
    except:
        marcador.configure(text="Coloque uma função de forma correta")

def integral():
    try:
        x = symbols('x')
        func_escrita2 = funcao.get()
        expr2 = parse_expr(func_escrita2)
        f = lambdify(x, expr2)
        result = quad(f, 0, 5)
        integral = integrate(expr2,x)
        marcador.configure(text=integral)
        marcador2.configure(text=result)
    except:
        marcador.configure(text="Coloque uma função de forma correta")


janela = Tk()
janela.geometry('800x600')
janela.title("Cálculo Diferencial e Integral: f(x)")

frase_p_usuario = Label(janela, text="Digite uma função de x: ", font=("Arial", 15), fg="purple")
frase_p_usuario.pack()

funcao = Entry(janela, font=("Arial", 15))
funcao.pack()

marcador = Label(janela, text="Resultado", font=("Arial", 15), fg="green")
marcador.pack()

marcador2 = Label(janela, text="", font=("Arial", 15), fg="orange")
marcador2.pack()

btn_1 = Button(janela, text="Derivar função", font=("Arial", 15), command=derivada)
btn_1.pack()

btn_2 = Button(janela, text="Integrar função", font=("Arial", 15), command=integral)
btn_2.pack()

def _quit(): # função de saída
    janela.quit() # possui o mainloop
    janela.destroy() # destrói a janela criada, tira ela da memória

btn_3 = Button(master=janela, text="Sair", font=("Arial", 15), command=_quit)
btn_3.pack()

janela.mainloop()
