# ComparadorOrdenacoes

Link para a documentação completa: https://docs.google.com/document/d/1hR3NpggJuWOQgsLCEWps9vnWkJkZMAhbWVppGM1tPhc/edit?usp=sharing

1. Este software foi programado em **Python** utilizando a biblioteca *Tkinter* de interface gráfica com o objetivo de demonstrar comparativamente as diferenças entre distintos algoritmos de ordenação.
  
2. O usuário pode selecionar qual algoritmo será utilizado, os valores de mínimo e máximo, a velocidade da ordenação e a quantidade de elementos a serem gerados. Os elementos são gerados aleatoriamente e possuem a chance de serem gerados de forma já ordenada.
   
3. Ao executar a ordenação, os passos são exibidos visualmente, demonstrando as comparações entre os elementos a serem ordenados até que todos estejam ordenados corretamente.



#### Exemplo do Bubble Sort

~~~python
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
~~~


![Exemplo](https://media.discordapp.net/attachments/1110968185525645367/1173344516183433368/image.png?ex=65639d3c&is=6551283c&hm=cf187aea358ea2778fadbed24522d992355b5f9d776080de1e8fb479ee5c761e&=&width=1276&height=633)

>Este projeto foi desenvolvido por alunos do Centro Universitário UDF para a disciplina de Computabilidade e complexidade de algoritmos.
>

Aluno | RGM
-------|------
[Guilherme Bastos](https://github.com/EGG1203) | 26651165
[Italo Santana](https://github.com/ItaloSantana2) | 28201108
[João Gabriel Souza Silva](https://github.com/JoaoGabrielSSilva) | 27909379
[João Victor Souza](https://github.com/vicsouz) | 27972950


