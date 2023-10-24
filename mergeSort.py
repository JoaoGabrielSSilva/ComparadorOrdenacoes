import time

def OrdenaMescla(dados, desenharDados, timeTick):
  OrdenaMesclaAlgoritmo(dados, 0, len(dados)-1, desenharDados, timeTick)


def OrdenaMesclaAlgoritmo(dados, esquerda, direita, desenharDados, timeTick):
  if esquerda < direita:
    meio = (esquerda + direita) // 2
    OrdenaMesclaAlgoritmo(dados, esquerda, meio, desenharDados, timeTick)
    OrdenaMesclaAlgoritmo(dados, meio + 1, direita, desenharDados, timeTick)
    Mesclar(dados, esquerda, meio, direita, desenharDados, timeTick)

def Mesclar(dados, esquerda, meio, direita, desenharDados, timeTick):
  desenharDados(dados, pegarListaCores(len(dados), esquerda, meio, direita))
  time.sleep(timeTick)

  ladoEsquerdo = dados[esquerda: meio + 1]
  ladoDireito = dados[meio + 1: direita + 1]

  indiceEsquerdo = indiceDireito = 0

  for indiceDados in range(esquerda, direita + 1):
    if indiceEsquerdo < len(ladoEsquerdo) and indiceDireito < len(ladoDireito):
      if ladoEsquerdo[indiceEsquerdo] <= ladoDireito[indiceDireito]:
        dados[indiceDados] = ladoEsquerdo[indiceEsquerdo] #talvez cause erro
        indiceEsquerdo += 1
      else: 
        dados[indiceDados] = ladoDireito[indiceDireito]
        indiceDireito += 1
    elif indiceEsquerdo < len(ladoEsquerdo):
      dados[indiceDados] = ladoEsquerdo[indiceEsquerdo]
      indiceEsquerdo += 1
    else:
      dados[indiceDados] = ladoDireito[indiceDireito]
      indiceDireito += 1
  desenharDados(dados, ["green" if x >= esquerda and x <= direita else "white" for x in range(len(dados))])
  time.sleep(timeTick)

def pegarListaCores(tamanho, esquerda, meio, direita ):
  listaCores = []
  for i in range(tamanho):
    if i >= esquerda and i <= direita:
      if i >= esquerda and i <= meio:
        listaCores.append("yellow")
      else:
        listaCores.append("pink")
    else:
      listaCores.append("white")

  return listaCores
