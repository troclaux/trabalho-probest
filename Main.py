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
    print('media: ', media)

def calcula_probabilidade(x):
    probabilidade = math.factorial(x-1)/pow(10,x-1)
    print('probabilidade: ', probabilidade)
    return probabilidade

def calcula_esperanca():
    esperanca = float(0)
    for i in range(11):
        esperanca = esperanca + (i+1)*calcula_probabilidade(i+1)
    print('esperanca: ', esperanca)
    return esperanca

def checa_se_todos_os_itens_da_lista_sao_1(lista):
    for i in lista:
        if i != 1:
            return False
    return True

def simula_questao_4(numero_simulacoes):
    for i in range(numero_simulacoes):
        posicao = None
        #vetor com as posicoes de cada nó iniciadas em 0, exceto a posição 0, que é onde a partícula inicia
        nodes = [1,0,0,0,0,0]
        #nodes[i] = 0 := ainda não passou pela posição i
        #nodes[i] = 1 := já passou pela posição i

        movimentos = 0
        #numero de movimentos comeca em zero

        movimentosMinimosPraVisitarTodasAsPosicoes = 0

        posicaoAtual = 0
        #posicao inicial eh zero
        proximaPosicao = None
        #variável binária que diz se a próxima posição vai ser i+1 ou i-1

        while(checa_se_todos_os_itens_da_lista_sao_1(nodes)):
            proximaPosicao = randint(0,1)
            if proximaPosicao == 0:
                posicaoAtual = posicaoAtual - 1
            else: 
                posicaoAtual = posicaoAtual + 1
            if posicaoAtual == 6:
                posicaoAtual = 0
            #checar se posso colocar um elif ao inves de if na linha abaixo
            if posicaoAtual == -1:
                posicaoAtual = 5
            if nodes[posicaoAtual] == 0:
                nodes[posicaoAtual] = 1
            movimentos = movimentos + 1
            #checar se tem numero de iteracoes correto
            for j in range(4):
                if nodes[j] == 0:
                    break
                    #se ainda tiver alguma posição não visitada, nem preciso olhar as outras
                movimentosMinimosPraVisitarTodasAsPosicoes = movimentos
        return movimentosMinimosPraVisitarTodasAsPosicoes

#simula_questao_1(100)
calcula_probabilidade(4)
calcula_esperanca()