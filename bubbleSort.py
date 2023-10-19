import time

def OrdenaBolha(dados, desenharDados, timeTick):
  for _ in range(len(dados)-1):
    for j in range(len(dados)-1):
      if dados[j] > dados[j+1]:
        dados[j], dados[j+1] = dados[j+1], dados[j]
        desenharDados(dados, ['green' if x == j or x == j+1 else 'yellow' for x in range(len(dados))])
        time.sleep(timeTick)
  desenharDados(dados, ['green' for x in range(len(dados))])
