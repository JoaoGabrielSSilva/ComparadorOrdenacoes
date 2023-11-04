import time
# Função de ordenação do Bubble Sort

def OrdenaBolha(dados, desenharDados, timeTick):
  passos = 0 #incializando o contador de passos  
  for _ in range(len(dados)-1): # Loop para percorrer a lista (len(dados) - 1) vezes    
    for j in range(len(dados)-1): # Loop para comparar pares de elementos adjacentes      
      if dados[j] > dados[j+1]: # Se o elemento atual for maior que o próximo, troca
        dados[j], dados[j+1] = dados[j+1], dados[j]
        desenharDados(dados, ['green' if x == j or x == j+1 else 'yellow' for x in range(len(dados))]) # Chama a função desenharDados para atualizar a interface, destacando os elementos comparados em verde   
        time.sleep(timeTick) # Pausa a execução por um curto período para controlar a velocidade da visualização
        passos += 1

 # Após a ordenação, desenha todos os elementos em verde para indicar a conclusão do processo        
  desenharDados(dados, ['green' for x in range(len(dados))])
  return passos
  
