import forca_final
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if (jogo == 1):
        print('Jogando forca')
        forca_final.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()

#Com isso vimos como diferenciar se o programa é o principal ou não,
#se ele está sendo executado diretamente ou só sendo importado.
#Na hora de importar um arquivo, ele lê o código da função, mas não o executa, pois ele não é o arquivo principal





'''
# def nome_da_funcao():
#   todo o código identado faz parte da função
#   print("aprendendo funções") Repare que uma função pode chamar uma outra função. print também é uma função e usamos ela dentro da nossa própria função.
#
#
#Uma função também pode receber parâmetros e retornar algum valor, por exemplo:

def soma(a, b):
     return a + b
A função soma recebe dois parâmetros (a e b) e retorna a soma. Ao chamar a função, podemos capturar o retorno:

s = soma(3, 4) 
#
'''