import time

global passos  # Variável global para contar os passos

# Função principal para iniciar a ordenação pelo Quick Sort
def OrdenaRapidoPrincipal(dados, cabeca, ponta, desenharDados, timeTick):
    global passos
    passos = 0
    OrdenaRapido(dados, cabeca, ponta, desenharDados, timeTick)
    return passos

# Função para realizar a partição do array
def particao(dados, cabeca, ponta, desenharDados, timeTick):
    global passos
    borda = cabeca
    pivot = dados[ponta]

    # Atualiza a exibição dos dados no canvas para destacar as partes a serem particionadas
    desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, borda))
    time.sleep(timeTick)

    for j in range(cabeca, ponta):
        if dados[j] < pivot:
            # Atualiza a exibição dos dados no canvas para destacar os elementos sendo trocados
            desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, j, True))
            time.sleep(timeTick)
            dados[borda], dados[j] = dados[j], dados[borda]
            borda += 1
            passos += 1

        # Atualiza a exibição dos dados no canvas
        desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, j))
        time.sleep(timeTick)

    # Atualiza a exibição dos dados no canvas para destacar a partição completa
    desenharDados(dados, pegarListaCores(len(dados), cabeca, ponta, borda, ponta, True))
    time.sleep(timeTick)
    # Trocando o pivô pelo valor na borda
    dados[borda], dados[ponta] = dados[ponta], dados[borda]
    passos += 1
    return borda

# Função principal para o Quick Sort
def OrdenaRapido(dados, cabeca, ponta, desenharDados, timeTick):
    global passos
    if cabeca < ponta:
        indiceParticao = particao(dados, cabeca, ponta, desenharDados, timeTick)

        # Partição da esquerda
        OrdenaRapido(dados, cabeca, indiceParticao - 1, desenharDados, timeTick)

        # Partição da direita
        OrdenaRapido(dados, indiceParticao + 1, ponta, desenharDados, timeTick)
    return passos

# Função para obter a lista de cores para destacar as partes do array
def pegarListaCores(qtdDados, cabeca, ponta, borda, indiceAtual, estaTrocando=False):
    listaCores = []
    for i in range(qtdDados):
        # Colorindo a base
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
