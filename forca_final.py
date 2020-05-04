import random
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()#Mas precisamos remover o \n ao final da linha, fazendo um strip
        palavras.append(linha) #coloca dentro da lista de palavras chamando a funçao append a lista

    arquivo.close()

    #print(palavras)
    #numero gerado com len pego tamanho lista e numero recebe o numero aleatoriamente gerado
    numero = random.randrange(0, len(palavras))
    palavra_secreta =palavras[numero].upper()
    #palavra secreta é palavras na posicao numero


    #palavra_secreta = "banana".upper()
   # letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_acertadas = ["_" for letra in palavra_secreta]
    # para cada letra dentro da palavra
    #for letra in palavra_secreta:
        #letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0
    #enquanto(True) não acertou e não enforcou
    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        #strip remove todos espaços em branco
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                #index = index + 1
                index += 1
            print(letras_acertadas)

        else:
            #erros = erros + 1
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))
        enforcou = erros == 6
        # enquanto a lista não possui o _, significa que a palavra ainda não foi totalmente preenchida
        acertou = "_" not in letras_acertadas

        if (acertou):
            print("Você ganhou!")
        else:
            print("Você errou!")


    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()



'''
>>> palavra = "banana"
>>> palavra.find("b")
0
>>> palavra.find("n")
2
>>> palavra = "banana"
>>> palavra.find("z")
-1

for variavel in lista
comandos
Enquanto percorremos a lista de valores, 
a variável indicada no for receberá, a cada iteração, um item da coleção.

>>> palavra = "aluracursos"
>>> palavra.find("a",1) #procurando "a" a partir da segunda posição 
4

Uma palavra nada mais é do que uma sequência de caracteres. 
Tanto isso é verdade, que podemos usar o laço for para iterar.
Nesse contexto iterar significa receber em cada iteração uma letra da palavra.

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada)) 
    
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    Essa funcionalidade do Python se chama List Comprehension, em português, Compreensão de lista.
    Queremos que a inicialização da lista de palavras acertadas seja dinâmica, baseada na quantidade de letras que
     houver na palavra secreta. Já sabemos implementar isso, podemos criar a lista vazia, e para cada letra 
     na palavra secreta, adicionamos um _ à ela:
     
     inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
        
        inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim ...
Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só:
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
'''