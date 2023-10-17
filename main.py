from tkinter import *
from tkinter import ttk
import random

#
root = Tk()
#
root.title('Visualização de Algoritmos de Ordenação')
#
root.maxsize(900, 600)
#
root.config(bg='black')

#Variáveis
algoritmo_selecionado = StringVar()

#Funções

def desenharDados(dados):
  canvas.delete("all")
  alturaCanvas = 380
  larguraCanvas = 600
  larguraBarras = larguraCanvas / (len(dados) + 1)
  #Para evitar que as barras sejam criadas tocando a borda
  deslocamento = 10
  espacamento = 10
  dadosNormalizados = [i / max(dados) for i in dados]
  for i, altura in enumerate(dadosNormalizados):
    #superior esquerda
    x0 = i * larguraBarras + deslocamento + espacamento
    y0 = alturaCanvas - altura * 340
    #inferior direita
    x1 = (i + 1) * larguraBarras + deslocamento
    y1 = alturaCanvas
    canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")
    canvas.create_text(x0 + 2, y0, anchor=SW, text=str(dados[i]))

def Gerar():
  print("Algoritmo Selecionado: " + algoritmo_selecionado.get())
  try:
    valMin = int(entradaMinimo.get())
  except:
    valMin = 1
  try:
    valMax = int(entradaMaximo.get())
  except:
    valMax = 10
  try:
    tamanho = int(entradaTamanho.get())
  except:
    tamanho = 10

  if valMin < 0 : valMin = 0
  if valMax > 100 : valMax = 100
  if tamanho > 30 or tamanho < 3: tamanho = 25
  if valMin > valMax : valMin, valMax = valMax, valMin
  
  dados = []
  for _ in range(tamanho):
    dados.append(random.randrange(valMin, valMax + 1))

  desenharDados(dados)

#Quadro / Layout base
#
frameInterface = Frame(root, width=200, height=380, bg='grey')
frameInterface.grid(row=0, column=0, padx=5, pady=5)

#
canvas = Canvas(root, width=550, height=380, bg='white')
canvas.grid(row=0, column=1, padx=5, pady=5 )

#Parte da Interface do Usuário
#Linha 0
#
Label(frameInterface, text="Algoritmo: ", bg='grey').grid(row=0, column=0, padx=5, sticky=W)
menuAlgoritmo = ttk.Combobox(frameInterface, textvariable=algoritmo_selecionado, values=['Bubble Sort', 'Merge Sort'])
menuAlgoritmo.grid(row=0, column=1, padx=5, pady=5)
menuAlgoritmo.current(0)
Button(frameInterface, text="Gerar", command= Gerar, bg='red').grid(row=0, column=2, padx=5, pady=5)
#Linha 1
#Campo de texto "Tamanho"
Label(frameInterface, text="Tamanho: ", bg='grey').grid(row=1, column=0, padx=5, sticky=W)
entradaTamanho = Entry(frameInterface)
entradaTamanho.grid(row=1, column=1, padx=5, pady=5, sticky=W)
#Campo de texto "Valor Mínimo"
Label(frameInterface, text="Valor Mínimo: ", bg='grey').grid(row=2, column=0, padx=5, sticky=W)
entradaMinimo = Entry(frameInterface)
entradaMinimo.grid(row=2, column=1, padx=5, pady=5, sticky=W)
#Campo de texto "Valor Máximo"
Label(frameInterface, text="Valor Máximo: ", bg='grey').grid(row=3, column=0, padx=5, sticky=W)
entradaMaximo = Entry(frameInterface)
entradaMaximo.grid(row=3, column=1, padx=5, pady=5, sticky=W)
#
root.mainloop()
