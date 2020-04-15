def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    #enquanto(True) não acertou e não enforcou
    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        #strip remove todos espaços em branco
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print(letras_acertadas)

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
'''