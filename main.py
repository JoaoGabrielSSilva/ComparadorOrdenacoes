from tkinter import *
from tkinter import ttk
import random
from bubbleSort import OrdenaBolha  # Importa uma função "OrdenaBolha" do outro arquivo (bubbleSort.py)
from quickSort import OrdenaRapido
from mergeSort import  OrdenaMescla
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
dadosSalvos = []

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
    global dadosSalvos
    valMin = int(entradaMinimo.get())
    valMax = int(entradaMaximo.get())
    tamanho = int(entradaQuantidade.get())

    dados = []
    #Gera um valor aleatório na quantidade especificada
    for _ in range(tamanho):
        dados.append(random.randrange(valMin, valMax + 1))
    
    #Cada valor gerado é passado para a lista dadosSalvos para ter a possibilidade de reiniciar a ordenação
    for i in range(tamanho):
        dadosSalvos.append(dados[i])
    
    desenharDados(dados, ['yellow' for x in range(len(dados))])

#Função para reiniciar para a lista de dados inicial sem ordenação
def ReiniciarOrdenacao():
    global dadosSalvos
    global dados
    quantPassos.set(0)
    tamanho = int(entradaQuantidade.get())
    dados = []
    for _ in range(tamanho):
        dados.append(dadosSalvos[_])

    desenharDados(dados, ['yellow' for x in range(len(dados))])
    
# Função para iniciar o algoritmo de ordenação
def IniciarAlgoritmo():
    global dados
    if not dados: return

    #Escolha do algoritmo de ordenação
    if menuAlgoritmo.get() == 'Quick Sort':
        OrdenaRapido(dados, 0, len(dados) - 1, desenharDados, escalaVelocidade.get())
    elif menuAlgoritmo.get() == 'Bubble Sort':
        quantPassos.set(OrdenaBolha(dados, desenharDados, escalaVelocidade.get()))
    elif menuAlgoritmo.get() == 'Merge Sort':
        quantPassos.set(OrdenaMescla(dados, desenharDados, escalaVelocidade.get()))
    desenharDados(dados, ['green' for x in range(len(dados))])
# Criação da interface
frameInterface = Frame(root, width=200, height=380, bg='grey')
frameInterface.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=0, column=1, padx=5, pady=5)

# Parte da Interface do Usuário
# Linha 0

Label(frameInterface, text="Algoritmo: ", bg='grey').grid(row=0, column=0, padx=5, sticky=W)
menuAlgoritmo = ttk.Combobox(frameInterface, textvariable=algoritmo_selecionado, values=['Bubble Sort','Quick Sort', 'Merge Sort' ])
menuAlgoritmo.grid(row=0, column=1, padx=5, pady=5)
menuAlgoritmo.current(0)

#Contador de Passos
Label(frameInterface, text="Passos: ", bg='grey').grid(row=1, column=0, padx=5, sticky=W)
Label(frameInterface, textvariable= quantPassos, bg='grey').grid(row=1, column=1, padx=5, sticky=W)

#Botão para reiniciar a ordenação
Button(frameInterface, text="Reset", command=ReiniciarOrdenacao, bg='red').grid(row=2, column=0, padx=5, pady=5)

# Campo de texto "Valor Mínimo"
entradaMinimo = Scale(frameInterface, from_=0, to=10, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Mínimo")
entradaMinimo.grid(row=3, column=0, padx=5, pady=5)

# Campo de texto "Valor Máximo"
entradaMaximo = Scale(frameInterface, from_=10, to=100, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Máximo")
entradaMaximo.grid(row=3, column=1, padx=5, pady=5)

#Velocidade
escalaVelocidade = Scale(frameInterface, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=VERTICAL, label="Velocidade(s)")
escalaVelocidade.grid(row=4, column=0, padx=5, pady=5)

# Campo de texto "Quantidade"
entradaQuantidade = Scale(frameInterface, from_=25, to=3, digits=2, resolution=1, orient=VERTICAL, label="Quantidade")
entradaQuantidade.grid(row=4, column=1, padx=5, pady=5)

#Botão para gerar um conjunto de dados
Button(frameInterface, text="Gerar", command=Gerar, bg='white').grid(row=5, column=0, padx=5, pady=5)

#Botão para iniciar a ordenação
Button(frameInterface, text="Iniciar", command=IniciarAlgoritmo, bg='green').grid(row=5, column=1, padx=5, pady=5)



root.mainloop()
