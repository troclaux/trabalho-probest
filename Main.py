#questao 1.a = P(X=x) = (x-1)/10
#E(X) = 1*(0/10) + 2*(1/10) + 3*(2/10) + 4*(3/10) + 5*(4/10) + 6*(5/10) + 7*(6/10) + 8*(7/10) + 9*(8/10) + 10*(9/10) + 11*(10/10)

from random import randint

def simula_questao_1(numero_de_simulacoes):
    bolas_sorteadas = [False] * 11
    print(str(bolas_sorteadas))
    #loop para simular a quantidade de vezes desejada
    for i in range(numero_de_simulacoes):
        #enquanto nao sortear um numero igual
        x = 0
        for j in range(11):
            x+=1
            bola_sorteada = randint(1, 10)
            print('bola sorteada: ', bola_sorteada)
            if( bolas_sorteadas[bola_sorteada-1] == True ):
                print("x: ", x)
                return x
            bolas_sorteadas[bola_sorteada-1] = True

simula_questao_1(1)