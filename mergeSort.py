import time

global passos  # Variável global para contar os passos

# Função para realizar a ordenação por Mescla (Merge Sort)
def OrdenaMescla(dados, desenharDados, timeTick):
    global passos
    passos = 0
    OrdenaMesclaAlgoritmo(dados, 0, len(dados) - 1, desenharDados, timeTick)
    return passos

# Função principal para a ordenação por Mescla (Merge Sort)
def OrdenaMesclaAlgoritmo(dados, esquerda, direita, desenharDados, timeTick):
    global passos
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        # Chama a função recursivamente para a metade esquerda
        OrdenaMesclaAlgoritmo(dados, esquerda, meio, desenharDados, timeTick)
        # Chama a função recursivamente para a metade direita
        OrdenaMesclaAlgoritmo(dados, meio + 1, direita, desenharDados, timeTick)
        # Realiza a mescla das duas metades
        Mesclar(dados, esquerda, meio, direita, desenharDados, timeTick)
        passos += 1

# Função para mesclar duas partes ordenadas do array
def Mesclar(dados, esquerda, meio, direita, desenharDados, timeTick):
    # Atualiza a exibição dos dados no canvas para destacar as partes sendo mescladas
    desenharDados(dados, pegarListaCores(len(dados), esquerda, meio, direita))
    time.sleep(timeTick)

    # Divide o array em duas partes
    ladoEsquerdo = dados[esquerda: meio + 1]
    ladoDireito = dados[meio + 1: direita + 1]

    indiceEsquerdo = indiceDireito = 0

    for indiceDados in range(esquerda, direita + 1):
        if indiceEsquerdo < len(ladoEsquerdo) and indiceDireito < len(ladoDireito):
            if ladoEsquerdo[indiceEsquerdo] <= ladoDireito[indiceDireito]:
                dados[indiceDados] = ladoEsquerdo[indiceEsquerdo]
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
    
    # Atualiza a exibição dos dados no canvas para realçar a parte ordenada em verde
    desenharDados(dados, ["green" if x >= esquerda and x <= direita else "white" for x in range(len(dados))])
    time.sleep(timeTick)

# Função para obter a lista de cores para destacar as partes a serem mescladas
def pegarListaCores(tamanho, esquerda, meio, direita):
    listaCores = []
    for i in range(tamanho):
        if i >= esquerda and i <= direita:
            if i >= esquerda and i <= meio:
                listaCores.append("yellow")  # Marca a parte esquerda a ser mesclada em amarelo
            else:
                listaCores.append("pink")  # Marca a parte direita a ser mesclada em rosa
        else:
            listaCores.append("white")  # Mantém o resto em branco

    return listaCores
