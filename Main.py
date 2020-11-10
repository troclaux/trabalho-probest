#questao 1.a = P(X=x) = (factorial(9) * (x-1))/(factorial(11-x) * pow(10,(x-1))), para 1 < x < 12
#E(X) = 1*(0/10) + 2*(1/10) + 3*(2/10) + 4*(3/10) + 5*(4/10) + 6*(5/10) + 7*(6/10) + 8*(7/10) + 9*(8/10) + 10*(9/10) + 11*(10/10)

from random import randint
import math
from scipy import random
import numpy

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
            #caso a bola sorteada seja repetida
            if( bolas_sorteadas[bola_sorteada] == True ):
                media = media + x
                print(str(bolas_sorteadas))
                print("x: ", x)
                lista_dos_x.append(x)
                break
            bolas_sorteadas[bola_sorteada] = True
    media = media/numero_de_simulacoes
    print(str(lista_dos_x))
    print('Media das simulações: ', media)

def calcula_probabilidade(x):
    if(x > 11):
        return 0
    probabilidade = float(1)
    buffer = 9
    for i in range(2, x + 1):
        if i == x:
            probabilidade = probabilidade * (x - 1)/10
        else:
            probabilidade = probabilidade * (buffer/10)
            buffer = buffer - 1
        # print(i)
    return probabilidade

def calcula_esperanca():
    esperanca = float(0)
    for i in range(2,12):
        esperanca = esperanca + (i)*calcula_probabilidade(i)
    print('Esperança: ', esperanca)
    return esperanca


def FuncaoQuestao3(x):
    return 4*(x**2)*math.exp(-3*x**2)
    
def MonteCarlo():
    a = -99999
    b = 99999

    somatorio = 0.0

    N = 10000
    pontos = numpy.zeros(N)

    for i in range(len(pontos)):
        pontos[i] = random.uniform(a,b)
        #vetor com os pontos selecionados aleatoriamente
    
    for i in range(N):
        somatorio += FuncaoQuestao3(pontos[i])
        
    integralAproximada = ((b-a)/float(N))*somatorio
    
    return integralAproximada

def Simula_Questao3(k):
    resultadoSimulacao = 0

    for i in range(k):
        resultadoSimulacao = MonteCarlo()
        print("Simulacao ", i, ": ", resultadoSimulacao, "\n")

# simula_questao_1(5000)
# calcula_probabilidade(11)
# calcula_esperanca()
Simula_Questao3(5000)