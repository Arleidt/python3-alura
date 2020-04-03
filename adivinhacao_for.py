print("********************************")
print('Bem Vindo ao Jogo de Adivinhação')
print("********************************")

numero_secreto = 42
total_tentativas = 3
#para variável em série de valores:
#  faça algo
for rodada in range(1, total_tentativas +1):
    print('tentativa {} de {}'.format(rodada,total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
#Esse comando faz com que a iteração do laço acabe, e comece a próxima continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
#if(numero_secreto == chute):
    if(acertou):
        print('Você acertou')
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")
print('Fim do Jogo')

#se numero secreto == chute
#print("vc acertou")
#senao
#print("voce errou")

'''
>>> for rodada in range(1,10):
...     print(rodada)
... 
1
2
3
4
5
6
7
8
9
Só imprimirá de 1 até 9, porque a última posição do range é não-inclusiva.

Utilizando o range com um step 2.
>>> for rodada in range(1,10,2):
...     print(rodada)
... 
1
3
5
7
9

>>> for rodada in [1,2,3,4,5]:
...     print(rodada)
... 
1
2
3
4
5
A função range possui os seguintes parâmetros:

range(start, stop, [step])
Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:

for contador in range(1,11,3):
    print(contador)
break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
'''