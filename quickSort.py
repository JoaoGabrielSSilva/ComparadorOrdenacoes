import time
def particao(dados, cabeca, ponta, desenharDados, timeTick):
  borda = cabeca
  pivot = dados[ponta]

  desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, borda))
  time.sleep(timeTick)
  for j in range(cabeca, ponta):
    if dados[j] < pivot:
      desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, j, True))
      time.sleep(timeTick)
      dados[borda], dados[j] = dados[j], dados[borda] 
      borda += 1

    desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, j))
    time.sleep(timeTick)

  desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, ponta, True))
  time.sleep(timeTick)
  #trocando o pivô pelo valor da borda  
  dados[borda], dados[ponta] = dados[ponta], dados[borda]
  return borda

def OrdenaRapido(dados, cabeca, ponta, desenharDados, timeTick):
  if cabeca < ponta:
    indiceParticao = particao(dados, cabeca, ponta, desenharDados, timeTick)

    #Partição da esquerda
    OrdenaRapido(dados, cabeca, indiceParticao - 1, desenharDados, timeTick)

    #Partição da direita
    OrdenaRapido(dados, indiceParticao + 1, ponta, desenharDados, timeTick)

def pegarListaCores(qtdDados, cabeca, ponta, borda, indiceAtual,  estaTrocando = False):
  listaCores = []
  for i in range(qtdDados):
    #colorindo a base
    if i >= cabeca and i <= ponta:
      listaCores.append('gray')
    else:
      listaCores.append('green')

    if i == ponta:
      listaCores[i] = 'blue'
    elif i == borda:
      listaCores[i] = 'red'
    elif i == indiceAtual:
      listaCores[i] = 'yellow'

    if estaTrocando:
      if i == borda or i == indiceAtual:
        listaCores[i] = 'green'

  return listaCores
