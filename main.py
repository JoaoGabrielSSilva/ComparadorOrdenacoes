from tkinter import *
from tkinter import ttk
import random
from bubbleSort import OrdenaBolha  # Importa uma função "OrdenaBolha" do outro arquivo (bubbleSort.py)

# Inicializa a janela principal
root = Tk()

# Configurações da janela
root.title('Visualização de Algoritmos de Ordenação')
root.maxsize(900, 600)
root.config(bg='black')

# Variáveis
algoritmo_selecionado = StringVar()
dados = []
quantPassos = IntVar()
quantPassos.set(0)

# Função para desenhar os dados na interface
def desenharDados(dados, listaCores):
    canvas.delete("all")
    alturaCanvas = 380
    larguraCanvas = 600
    larguraBarras = larguraCanvas / (len(dados) + 1)
    deslocamento = 10
    espacamento = 10
    dadosNormalizados = [i / max(dados) for i in dados]

    for i, altura in enumerate(dadosNormalizados):
        x0 = i * larguraBarras + deslocamento + espacamento
        y0 = alturaCanvas - altura * 340
        x1 = (i + 1) * larguraBarras + deslocamento
        y1 = alturaCanvas
        canvas.create_rectangle(x0, y0, x1, y1, fill=listaCores[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(dados[i]))
    root.update_idletasks()

# Função para gerar dados aleatórios
def Gerar():
    global dados
    valMin = int(entradaMinimo.get())
    valMax = int(entradaMaximo.get())
    tamanho = int(entradaQuantidade.get())

    dados = []
    for _ in range(tamanho):
        dados.append(random.randrange(valMin, valMax + 1))

    desenharDados(dados, ['yellow' for x in range(len(dados))])

# Função para iniciar o algoritmo de ordenação
def IniciarAlgoritmo():
    global dados
    quantPassos.set(OrdenaBolha(dados, desenharDados, escalaVelocidade.get()))

# Criação da interface
frameInterface = Frame(root, width=200, height=380, bg='grey')
frameInterface.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=0, column=1, padx=5, pady=5)

# Parte da Interface do Usuário
# Linha 0

Label(frameInterface, text="Algoritmo: ", bg='grey').grid(row=0, column=0, padx=5, sticky=W)
menuAlgoritmo = ttk.Combobox(frameInterface, textvariable=algoritmo_selecionado, values=['Bubble Sort', 'Merge Sort'])
menuAlgoritmo.grid(row=0, column=1, padx=5, pady=5)
menuAlgoritmo.current(0)

#Contador de Passos
Label(frameInterface, text="Passos: ", bg='grey').grid(row=1, column=0, padx=5, sticky=W)
Label(frameInterface, textvariable= quantPassos, bg='grey').grid(row=1, column=1, padx=5, sticky=W)

#Tempo decorrido
Label(frameInterface, text= "Tempo decorrido: ", bg='grey').grid(row=2, column=0, padx=5, sticky=W)

#Velocidade
escalaVelocidade = Scale(frameInterface, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=VERTICAL, label="Velocidade")
escalaVelocidade.grid(row=4, column=0, padx=5, pady=5)

Button(frameInterface, text="Iniciar", command=IniciarAlgoritmo, bg='red').grid(row=5, column=1, padx=5, pady=5)

# Linha 1
# Campo de texto "Quantidade"
entradaQuantidade = Scale(frameInterface, from_=25, to=3, digits=2, resolution=1, orient=VERTICAL, label="Quantidade")
entradaQuantidade.grid(row=4, column=1, padx=5, pady=5)

# Campo de texto "Valor Mínimo"
entradaMinimo = Scale(frameInterface, from_=0, to=10, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Mínimo")
entradaMinimo.grid(row=3, column=0, padx=5, pady=5)

# Campo de texto "Valor Máximo"
entradaMaximo = Scale(frameInterface, from_=10, to=100, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Máximo")
entradaMaximo.grid(row=3, column=1, padx=5, pady=5)

Button(frameInterface, text="Gerar", command=Gerar, bg='white').grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
