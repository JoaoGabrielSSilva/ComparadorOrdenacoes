import random #importando a biblioteca random para números aleatórios
import time #importando a biblioteca time para utilizar a variável de velocidade do algoritmo

def bogoSort(dados, desenharDados, timeTick):
    tamanho = len(dados) #armazenando a quantidade de dados
    passos = 0 #iniciando o contador de passos
    while(esta_ordenado(dados) == False): #enquanto não estiver ordenado
        embaralhar(dados) #embaralha a ordem dos dados
        desenharDados(dados, ['green' for x in range(len(dados))]) #desenhando os elementos na tela
        time.sleep(timeTick) #faz o programa aguardar por um tempo
        passos += 1 #soma 1 ao contador de passos ao realizar cada aleatorização
    return passos

def esta_ordenado(dados):
    #função que possui o objetivo de verificar se os dados estão em ordem
    tamanho = len(dados) #recebe a quantidade de dados
    for i in range(0, tamanho - 1): #de acordo com a quantidade, do índice 0 ao último
        if(dados[i] > dados[i+1]): return False #se o dado atual for maior que o próximo, não está ordenado
    return True# caso contrário, está ordenado

def embaralhar(dados):
    #função que realiza o embaralhamento dos dados
    tamanho = len(dados) #recebe a quantidade de dados
    for indice in range(0, tamanho):
        #para cada indice na lista de dados
        indiceAleatorio = random.randint(0, tamanho-1)#armazena um valor aleatório entre o primeiro índice(0) e o último índice len(dados) - 1
        dados[indice], dados[indiceAleatorio] = dados[indiceAleatorio], dados[indice] # troca os valores. O valor do índice atual recebe o valor de outro índice e o outro índice recebe o valor atual
