#questao 1.a = P(X=x) = (x-1)!/(10^(x-1))
#E(X) = 1*(0/10) + 2*(1/10) + 3*(2/10) + 4*(3/10) + 5*(4/10) + 6*(5/10) + 7*(6/10) + 8*(7/10) + 9*(8/10) + 10*(9/10) + 11*(10/10)

from random import randint
import math

def simula_questao_1(numero_de_simulacoes):
    lista_dos_x = []
    media = float(0)
    #loop para simular a quantidade de vezes desejada
    for i in range(numero_de_simulacoes):
        #enquanto nao sortear um numero igual
        #x vai ser o numero de repeticoes ate ser sorteada uma bola 2 vezes
        x = 0
        #vetor que vai armazenar as bolas que foram sorteadas
        bolas_sorteadas = [False] * 12
        for j in range(11):
            x=x+1
            bola_sorteada = randint(1, 10)
            print('bola sorteada: ', bola_sorteada)
            if( bolas_sorteadas[bola_sorteada] == True ):
                media = media + x
                print(str(bolas_sorteadas))
                print("x: ", x)
                lista_dos_x.append(x)
                break
            bolas_sorteadas[bola_sorteada] = True
    media = media/numero_de_simulacoes
    print(str(lista_dos_x))
    print('media: ', media)

def calcula_probabilidade(x):
    probabilidade = math.factorial(x-1)/pow(10,x-1)
    print('probabilidade: ', probabilidade)
    return probabilidade


#simula_questao_1(10)
calcula_probabilidade(4)